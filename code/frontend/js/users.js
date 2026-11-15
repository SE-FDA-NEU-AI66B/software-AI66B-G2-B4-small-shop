const API_BASE = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {
    // State
    let usersList = [];
    let resetRequestsList = [];

    // DOM Elements
    const usersTableBody = document.getElementById("usersTableBody");
    const resetRequestsBody = document.getElementById("resetRequestsBody");
    const resetRequestsPanel = document.getElementById("resetRequestsPanel");
    const resetRequestCount = document.getElementById("resetRequestCount");
    const totalUsersEl = document.getElementById("totalUsers");
    const totalManagersEl = document.getElementById("totalManagers");
    const userSearchInput = document.getElementById("userSearch");

    // Modal elements
    const userModal = document.getElementById("userModal");
    const openAddUserBtn = document.getElementById("openAddUserBtn");
    const closeUserModalBtn = document.getElementById("closeUserModalBtn");
    const cancelUserModalBtn = document.getElementById("cancelUserModalBtn");
    const userForm = document.getElementById("userForm");
    const userModalTitle = document.getElementById("userModalTitle");
    const userIdInput = document.getElementById("userId");
    const userUsernameInput = document.getElementById("userUsername");
    const userRoleInput = document.getElementById("userRole");
    const defaultPasswordNote = document.getElementById("defaultPasswordNote");

    // Initialize data loading
    loadAllData();

    // Event Listeners
    if (openAddUserBtn) {
        openAddUserBtn.addEventListener("click", () => openModalForCreate());
    }
    if (closeUserModalBtn) {
        closeUserModalBtn.addEventListener("click", () => closeModal());
    }
    if (cancelUserModalBtn) {
        cancelUserModalBtn.addEventListener("click", () => closeModal());
    }
    if (userModal) {
        userModal.addEventListener("click", (e) => {
            if (e.target === userModal) closeModal();
        });
    }
    if (userForm) {
        userForm.addEventListener("submit", handleSaveUser);
    }
    if (userSearchInput) {
        userSearchInput.addEventListener("input", (e) => filterAndRenderUsers(e.target.value));
    }

    // Load both Users and Pending Password Reset Requests
    async function loadAllData() {
        try {
            await fetchResetRequests();
            await fetchUsers();
        } catch (error) {
            console.error("Error loading data:", error);
        }
    }

    // 1. FETCH USERS (GET /users)
    async function fetchUsers() {
        try {
            const response = await fetch(`${API_BASE}/users`);
            if (!response.ok) throw new Error("Failed to load users");
            usersList = await response.json();
            renderUsers(usersList);
            updateKPIs(usersList);
        } catch (error) {
            console.error(error);
            usersTableBody.innerHTML = `<tr><td colspan="6" class="table-message" style="color: red;">Error loading users from server.</td></tr>`;
            showToast("Failed to fetch users", "error");
        }
    }

    // 2. FETCH PENDING RESET REQUESTS (GET /auth/password-reset-requests)
    async function fetchResetRequests() {
        try {
            const response = await fetch(`${API_BASE}/auth/password-reset-requests`);
            if (!response.ok) throw new Error("Failed to load reset requests");
            resetRequestsList = await response.json();
            renderResetRequests(resetRequestsList);
        } catch (error) {
            console.error(error);
            resetRequestsBody.innerHTML = `<tr><td colspan="4" class="table-message" style="color: red;">Error loading reset requests.</td></tr>`;
        }
    }

    // Render Users Table
    function renderUsers(data) {
        if (!data || data.length === 0) {
            usersTableBody.innerHTML = `<tr><td colspan="6" class="table-message">No users found.</td></tr>`;
            return;
        }

        usersTableBody.innerHTML = data.map(user => {
            // Check if user has a pending reset request
                const hasPendingRequest = resetRequestsList.some(req => Number(req.user_id) === Number(user.user_id));            const resetBadge = hasPendingRequest 
                ? `<span class="badge badge-warning" style="background:#fff3cd; color:#856404; padding:2px 8px; border-radius:4px; font-size:12px;">Reset Requested</span>` 
                : `<span style="color: #6c757d;">None</span>`;

            const createdAtFormatted = user.created_at ? new Date(user.created_at).toLocaleDateString() : 'N/A';

            return `
                <tr>
                    <td>US-${String(user.user_id).padStart(3, '0')}</td>
                    <td><strong>${escapeHtml(user.username)}</strong></td>
                    <td><span class="badge role-${user.role.toLowerCase()}">${escapeHtml(user.role)}</span></td>
                    <td>${createdAtFormatted}</td>
                    <td>${resetBadge}</td>
                    <td>
                        <div class="action-buttons">
                            <button type="button" class="btn-icon reset-btn" title="Reset Password" onclick="window.appResetPassword(${user.user_id}, '${escapeHtml(user.username)}')">
                                <i class="fa-solid fa-key"></i> Reset
                            </button>
                            <button type="button" class="btn-icon edit-btn" title="Edit User" onclick="window.appEditUser(${user.user_id})">
                                <i class="fa-solid fa-pen-to-square"></i>
                            </button>
                            <button type="button" class="btn-icon delete-btn" title="Delete User" onclick="window.appDeleteUser(${user.user_id})">
                                <i class="fa-solid fa-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        }).join("");
    }

    // Render Reset Requests Section
    function renderResetRequests(requests) {
        if (!requests || requests.length === 0) {
            if (resetRequestsPanel) resetRequestsPanel.hidden = true;
            return;
        }

        if (resetRequestsPanel) resetRequestsPanel.hidden = false;
        if (resetRequestCount) resetRequestCount.textContent = `${requests.length} pending`;

        resetRequestsBody.innerHTML = requests.map(req => {
            const requestedAt = req.requested_at ? new Date(req.requested_at).toLocaleString() : 'N/A';
            return `
                <tr>
                    <td><strong>${escapeHtml(req.username)}</strong></td>
                    <td>${escapeHtml(req.role || 'User')}</td>
                    <td>${requestedAt}</td>
                    <td>
                        <button type="button" class="btn-primary" style="padding: 4px 12px; font-size: 12px;" onclick="window.appApproveReset(${req.user_id})">
                            Approve Reset
                        </button>
                    </td>
                </tr>
            `;
        }).join("");
    }

    // Update KPI statistics
    function updateKPIs(data) {
        if (totalUsersEl) totalUsersEl.textContent = data.length;
        if (totalManagersEl) {
            const managersCount = data.filter(u => u.role === "Manager" || u.role === "Admin").length;
            totalManagersEl.textContent = managersCount;
        }
    }

    // Filter Users via Search Input
    function filterAndRenderUsers(query) {
        const lowerQuery = query.toLowerCase().trim();
        const filtered = usersList.filter(user => 
            user.username.toLowerCase().includes(lowerQuery) || 
            user.user_id.toString().includes(lowerQuery)
        );
        renderUsers(filtered);
    }

    // Modal Handlers
    function openModalForCreate() {
        if (userModalTitle) userModalTitle.textContent = "Add User";
        if (userIdInput) userIdInput.value = "";
        if (userForm) userForm.reset();
        if (defaultPasswordNote) defaultPasswordNote.style.display = "block";
        if (userModal) userModal.classList.add("active");
    }

    window.appEditUser = function(id) {
        const user = usersList.find(u => u.user_id === id);
        if (!user) return;

        if (userModalTitle) userModalTitle.textContent = "Edit User";
        if (userIdInput) userIdInput.value = user.user_id;
        if (userUsernameInput) userUsernameInput.value = user.username;
        if (userRoleInput) userRoleInput.value = user.role;
        if (defaultPasswordNote) defaultPasswordNote.style.display = "none"; // Password not editable here
        if (userModal) userModal.classList.add("active");
    }

    function closeModal() {
        if (userModal) userModal.classList.remove("active");
    }

    // 3. CREATE OR UPDATE USER (POST /users or PUT /users/{id})
    async function handleSaveUser(e) {
        e.preventDefault();
        const id = userIdInput.value;
        const payload = {
            username: userUsernameInput.value.trim(),
            role: userRoleInput.value
        };

        try {
            let response;
            if (id) {
                // UPDATE user (PUT /users/{user_id})
                response = await fetch(`${API_BASE}/users/${id}`, {
                    method: "PUT",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });
            } else {
                // CREATE user (POST /users)
                response = await fetch(`${API_BASE}/users`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });
            }

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.detail || "Failed to save user");
            }

            showToast(id ? "User updated successfully!" : "User created successfully!", "success");
            closeModal();
            loadAllData();
        } catch (error) {
            showToast(error.message, "error");
        }
    }

    // 4. DELETE USER (DELETE /users/{user_id})
    window.appDeleteUser = async function(id) {
        if (!confirm("Are you sure you want to delete this user?")) return;

        try {
            const response = await fetch(`${API_BASE}/users/${id}`, {
                method: "DELETE"
            });

            if (!response.ok && response.status !== 204) {
                throw new Error("Failed to delete user");
            }

            showToast("User deleted successfully", "success");
            loadAllData();
        } catch (error) {
            showToast(error.message, "error");
        }
    }

    // 5. ADMIN RESET USER PASSWORD DIRECTLY (POST /users/{user_id}/reset-password)
    window.appResetPassword = async function(id, username) {
        if (!confirm(`Are you sure you want to reset password for "${username}" back to default?`)) return;

        try {
            const response = await fetch(`${API_BASE}/users/${id}/reset-password`, {
                method: "POST"
            });

            if (!response.ok) throw new Error("Failed to reset password");

            const result = await response.json();
            showToast(result.message || "Password reset successfully.", "success");
        } catch (error) {
            showToast(error.message, "error");
        }
    }

    // 6. APPROVE PENDING PASSWORD RESET REQUEST (POST /auth/password-reset-requests/{user_id}/approve)
    window.appApproveReset = async function(userId) {
        if (!confirm("Approve password reset request for this user?")) return;

        try {
            const response = await fetch(`${API_BASE}/auth/password-reset-requests/${userId}/approve`, {
                method: "POST"
            });

            if (!response.ok) throw new Error("Failed to approve password reset");

            const result = await response.json();
            showToast(result.message || "Password reset approved successfully.", "success");
            loadAllData();
        } catch (error) {
            showToast(error.message, "error");
        }
    }

    // Utility: Toast notifications
    function showToast(message, type = "success") {
        const toast = document.getElementById("toastNotification");
        if (!toast) return;
        toast.textContent = message;
        toast.className = `toast show ${type}`;
        setTimeout(() => {
            toast.className = "toast";
        }, 3500);
    }

    // Utility: Prevent XSS
    function escapeHtml(str) {
        if (!str) return "";
        return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
    }
});