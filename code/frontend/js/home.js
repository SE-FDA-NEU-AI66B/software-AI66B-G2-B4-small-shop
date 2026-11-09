const menu_btn = document.querySelector(".menu-btn");
const main = document.querySelector(".main-content");
const sidebar = document.querySelector(".sidebar");

if (menu_btn && main && sidebar) {
    menu_btn.addEventListener("click", function() {
        main.classList.toggle("expand");
        sidebar.classList.toggle("hidden");
        menu_btn.classList.toggle("update");
    });
}

let authenticatedUser = {};
const userJson = sessionStorage.getItem("authenticatedUser");

if (userJson) {
    try {
        authenticatedUser = JSON.parse(userJson) || {};
    } catch (error) {
        console.error("Unable to read the authenticated user's profile.", error);
    }
}

const roleNames = {
    Admin: "Administrator",
    Manager: "Manager",
    Cashier: "Cashier",
    Staff: "Staff",
};
const username = authenticatedUser.username || "";
const role = roleNames[authenticatedUser.role] || authenticatedUser.role || "";
const initials = username
    .trim()
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map(part => part[0].toUpperCase())
    .join("");
const welcomeUsername = document.querySelector("#welcome-username");

if (welcomeUsername) {
    welcomeUsername.textContent = username;
}

let profile = document.querySelector(".user-profile, .account-card");
if (!profile) {
    const header = document.querySelector(".top-header, .page-header");
    if (header) {
        const actions = header.querySelector(".header-actions");
        profile = document.createElement("div");
        profile.className = "user-profile";
        profile.innerHTML = `
            <div class="user-avatar"></div>
            <div class="user-info">
                <div class="user-name"></div>
                <div class="user-role"></div>
            </div>
        `;
        (actions || header).append(profile);
        if (actions) {
            actions.classList.add("profile-actions");
        }
    }
}

if (profile) {
    const avatar = profile.querySelector(".user-avatar, .avatar");
    const name = profile.querySelector(".user-name, .role-name");
    const userRole = profile.querySelector(".user-role, .role-sub");

    if (avatar) avatar.textContent = initials;
    if (name) name.textContent = username;
    if (userRole) userRole.textContent = role;
    if (!profile.querySelector(".profile-chevron")) {
        const chevron = document.createElement("i");
        chevron.className = "fa-solid fa-chevron-down profile-chevron";
        chevron.setAttribute("aria-hidden", "true");
        profile.append(chevron);
    }

    const container = document.createElement("div");
    container.className = "profile-menu-container";
    profile.before(container);
    container.append(profile);

    profile.setAttribute("role", "button");
    profile.setAttribute("tabindex", "0");
    profile.setAttribute("aria-haspopup", "true");
    profile.setAttribute("aria-expanded", "false");
    profile.setAttribute("aria-controls", "profile-dropdown");

    const dropdown = document.createElement("div");
    dropdown.className = "profile-dropdown";
    dropdown.id = "profile-dropdown";
    dropdown.hidden = true;
    dropdown.innerHTML = `
        <section class="profile-dropdown-account" aria-label="Account Information">
            <h3>Account Information</h3>
            <strong class="profile-dropdown-name"></strong>
            <span class="profile-dropdown-role"></span>
            <small class="profile-dropdown-username"></small>
        </section>
        <div class="profile-dropdown-links">
            <button type="button" class="profile-dropdown-item">My Profile</button>
            <button type="button" class="profile-dropdown-item">Help</button>
        </div>
        <div class="profile-dropdown-logout">
            <button type="button" class="profile-dropdown-item">
                <i class="fa-solid fa-arrow-right-from-bracket" aria-hidden="true"></i>
                Log out
            </button>
        </div>
    `;
    container.append(dropdown);
    dropdown.querySelector(".profile-dropdown-name").textContent = username;
    dropdown.querySelector(".profile-dropdown-role").textContent = role;
    dropdown.querySelector(".profile-dropdown-username").textContent =
        authenticatedUser.username ? `@${authenticatedUser.username}` : "";

    const setDropdownOpen = isOpen => {
        dropdown.hidden = !isOpen;
        profile.setAttribute("aria-expanded", String(isOpen));
    };

    profile.addEventListener("click", () => {
        setDropdownOpen(dropdown.hidden);
    });
    profile.addEventListener("keydown", event => {
        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            setDropdownOpen(dropdown.hidden);
        }
    });
    document.addEventListener("click", event => {
        if (!container.contains(event.target)) {
            setDropdownOpen(false);
        }
    });
    document.addEventListener("keydown", event => {
        if (event.key === "Escape" && !dropdown.hidden) {
            setDropdownOpen(false);
            profile.focus();
        }
    });
    dropdown.querySelector(".profile-dropdown-logout").addEventListener("click", () => {
        sessionStorage.removeItem("authenticatedUser");
        window.location.href = "index.html";
    });
}
