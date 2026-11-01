const API_SALES_URL = "http://127.0.0.1:8000/sales";

function switchTab(tabName) {
  const tabs = document.querySelectorAll('.tab-content');
  const buttons = document.querySelectorAll('.tab-btn');

  tabs.forEach(tab => tab.classList.remove('active'));
  buttons.forEach(btn => btn.classList.remove('active'));

  if (tabName === 'overview') {
    document.getElementById('tab-overview').classList.add('active');
    document.getElementById('btn-overview').classList.add('active');
    fetchSalesOverview();
  } else if (tabName === 'prediction') {
    document.getElementById('tab-prediction').classList.add('active');
    document.getElementById('btn-prediction').classList.add('active');
    fetchPredictions();
  }
}

async function fetchSalesOverview() {
  const topNDropdown = document.getElementById('topNDropdown');
  const categoryInput = document.getElementById('categoryInput');

  const topN = topNDropdown ? topNDropdown.value : '5';
  const category = categoryInput ? categoryInput.value.trim() : '';

  let url = `${API_SALES_URL}/overview?top_n=${topN}`;
  if (category) url += `&category=${encodeURIComponent(category)}`;

  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to load sales overview.");
    const data = await response.json();
    renderSalesTable(data);
  } catch (error) {
    console.error(error.message);
  }
}

function renderSalesTable(dataToRender) {
  const tbody = document.getElementById('topSellingTableBody');
  if (!tbody) return;
  tbody.innerHTML = '';

  if (!dataToRender || dataToRender.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--text-muted); padding: 25px;">No matching items found</td></tr>`;
    return;
  }

  dataToRender.forEach((item) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td style="font-weight: 700; color: var(--text-muted);">#${item.rank}</td>
      <td style="font-weight: 600; color: var(--text-muted);">${item.id}</td>
      <td style="font-weight: 600; color: var(--bg-sidebar);">${item.name}</td>
      <td><span class="badge" style="background: #EAECEE; color: #2C3E50;">${item.category}</span></td>
      <td>${(item.units_sold_adjusted || 0).toLocaleString('en-US')} units</td>
      <td>${item.price.toLocaleString('en-US')} ₫</td>
      <td style="font-weight: 700; color: var(--bg-sidebar);">${(item.revenue_adjusted || 0).toLocaleString('en-US')} ₫</td>
      <td><span class="badge badge-success">${item.profit_margin || 40}%</span></td>
    `;
    tbody.appendChild(tr);
  });
}

async function fetchPredictions() {
  const selectElement = document.getElementById('predictionWindowSelect');
  const windowDays = parseInt(selectElement ? selectElement.value : "30");

  try {
    const response = await fetch(`${API_SALES_URL}/predictions?window_days=${windowDays}`);
    if (!response.ok) throw new Error("Failed to load predictions.");
    const data = await response.json();
    renderPredictionTable(data, windowDays);
  } catch (error) {
    console.error(error.message);
  }
}

function renderPredictionTable(dataToRender, windowDays) {
  const tbody = document.getElementById('predictionTableBody');
  if (!tbody) return;
  tbody.innerHTML = '';

  if (!dataToRender || dataToRender.length === 0) {
    tbody.innerHTML = `<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 25px;">No prediction data available</td></tr>`;
    return;
  }

  dataToRender.forEach(item => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td style="font-weight: 600; color: var(--text-muted);">${item.id}</td>
      <td style="font-weight: 600; color: var(--bg-sidebar);">${item.name}</td>
      <td>${item.current_stock} items</td>
      <td><strong>${item.predicted_demand}</strong> items / ${windowDays} days</td>
      <td style="color: var(--color-accent-red); font-weight: 700;">+${item.suggested_restock} items</td>
      <td>${item.status_badge}</td>
    `;
    tbody.appendChild(tr);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const topNDropdown = document.getElementById('topNDropdown');
  const categoryInput = document.getElementById('categoryInput');
  const timeframeFilter = document.getElementById('timeframeFilter');

  if (topNDropdown) topNDropdown.addEventListener('change', fetchSalesOverview);
  if (categoryInput) categoryInput.addEventListener('change', fetchSalesOverview);
  if (timeframeFilter) timeframeFilter.addEventListener('change', fetchSalesOverview);

  const btnReset = document.getElementById('btnResetFilter');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      if (topNDropdown) topNDropdown.value = '5';
      if (categoryInput) categoryInput.value = '';
      fetchSalesOverview();
    });
  }

  const btnOverview = document.getElementById('btn-overview');
  const btnPrediction = document.getElementById('btn-prediction');
  if (btnOverview) btnOverview.addEventListener('click', () => switchTab('overview'));
  if (btnPrediction) btnPrediction.addEventListener('click', () => switchTab('prediction'));

  const predictionSelect = document.getElementById('predictionWindowSelect');
  if (predictionSelect) predictionSelect.addEventListener('change', fetchPredictions);

  fetchSalesOverview();
});