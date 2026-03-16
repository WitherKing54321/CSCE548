const API_BASE = "http://127.0.0.1:8000";

window.addEventListener("DOMContentLoaded", () => {
  const baseUrlEl = document.getElementById("baseUrl");
  if (baseUrlEl) {
    baseUrlEl.textContent = API_BASE;
  }
});

function setStatus(message, type = "info") {
  const box = document.getElementById("statusMessage");
  if (!box) return;
  box.className = `status ${type}`;
  box.textContent = message;
}

function getValue(id) {
  const el = document.getElementById(id);
  return el ? el.value.trim() : "";
}

function clearResults() {
  const area = document.getElementById("resultsArea");
  if (area) area.innerHTML = "";
}

function showEmpty(message) {
  const area = document.getElementById("resultsArea");
  if (!area) return;
  area.innerHTML = `<div class="empty">${message}</div>`;
}

function safeText(value) {
  if (value === null || value === undefined || value === "") return "N/A";
  return String(value);
}

function titleCaseLabel(text) {
  return text
    .replace(/_/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

function parsePossiblyNestedData(data) {
  if (Array.isArray(data)) return data;
  if (data && Array.isArray(data.items)) return data.items;
  if (data && Array.isArray(data.data)) return data.data;
  return data;
}

function renderTable(items, preferredColumns = []) {
  const area = document.getElementById("resultsArea");
  if (!area) return;

  if (!Array.isArray(items) || items.length === 0) {
    showEmpty("No matching records were found.");
    return;
  }

  const allKeys = new Set();
  items.forEach(item => {
    if (item && typeof item === "object" && !Array.isArray(item)) {
      Object.keys(item).forEach(key => allKeys.add(key));
    }
  });

  let columns = preferredColumns.filter(col => allKeys.has(col));
  for (const key of allKeys) {
    if (!columns.includes(key)) {
      columns.push(key);
    }
  }

  const rowsHtml = items.map(item => `
    <tr>
      ${columns.map(col => `<td>${safeText(item[col])}</td>`).join("")}
    </tr>
  `).join("");

  area.innerHTML = `
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            ${columns.map(col => `<th>${titleCaseLabel(col)}</th>`).join("")}
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    </div>
  `;
}

function renderSingleObject(obj, title = "Record") {
  const area = document.getElementById("resultsArea");
  if (!area) return;

  if (!obj || typeof obj !== "object" || Array.isArray(obj)) {
    showEmpty("No matching record was found.");
    return;
  }

  const fields = Object.entries(obj).map(([key, value]) => `
    <tr>
      <th>${titleCaseLabel(key)}</th>
      <td>${safeText(value)}</td>
    </tr>
  `).join("");

  area.innerHTML = `
    <div class="item-card">
      <h3>${title}</h3>
      <div class="table-wrap">
        <table>
          <tbody>${fields}</tbody>
        </table>
      </div>
    </div>
  `;
}

function renderMessageCard(title, message) {
  const area = document.getElementById("resultsArea");
  if (!area) return;

  area.innerHTML = `
    <div class="item-card">
      <h3>${title}</h3>
      <p>${message}</p>
    </div>
  `;
}

function renderData(data, context = "") {
  const parsed = parsePossiblyNestedData(data);

  if (Array.isArray(parsed)) {
    if (context === "animeList" || context === "genreAnimeList") {
      renderTable(parsed, ["anime_id", "title", "release_year", "episodes", "studio_id", "studio_name"]);
      return;
    }

    if (context === "studiosList") {
      renderTable(parsed, ["studio_id", "name", "country"]);
      return;
    }

    if (context === "genresList" || context === "animeGenres") {
      renderTable(parsed, ["genre_id", "name"]);
      return;
    }

    renderTable(parsed);
    return;
  }

  if (parsed && typeof parsed === "object") {
    if (context === "animeSingle") {
      renderSingleObject(parsed, "Anime Details");
      return;
    }
    if (context === "studioSingle") {
      renderSingleObject(parsed, "Studio Details");
      return;
    }
    if (context === "genreSingle") {
      renderSingleObject(parsed, "Genre Details");
      return;
    }

    renderSingleObject(parsed, "Details");
    return;
  }

  renderMessageCard("Result", safeText(parsed));
}

async function callApi(path, options = {}, successMessage = "Request completed.", context = "") {
  setStatus("Loading...", "info");
  clearResults();

  try {
    const res = await fetch(API_BASE + path, options);

    const contentType = res.headers.get("content-type") || "";
    let body;

    if (contentType.includes("application/json")) {
      body = await res.json();
    } else {
      body = await res.text();
    }

    if (!res.ok) {
      const errorText = typeof body === "string" ? body : JSON.stringify(body);
      setStatus(`Request failed: ${res.status} ${res.statusText}`, "error");
      renderMessageCard("Error", errorText || "Something went wrong.");
      return null;
    }

    setStatus(successMessage, "success");

    if (typeof body === "string") {
      renderMessageCard("Server Response", body || "The action completed successfully.");
    } else {
      renderData(body, context);
    }

    return body;
  } catch (err) {
    setStatus("Could not connect to the API. Make sure the backend is running on port 8000.", "error");
    renderMessageCard("Connection Error", String(err));
    return null;
  }
}

function getAllAnime() {
  return callApi("/anime", {}, "Showing all anime.", "animeList");
}

function getAnimeById() {
  const id = getValue("animeId");
  if (!id) {
    setStatus("Please enter an Anime ID first.", "error");
    showEmpty("Enter an Anime ID, then click Find Anime.");
    return;
  }
  return callApi(`/anime/${id}`, {}, `Showing anime with ID ${id}.`, "animeSingle");
}

function getGenresForAnime() {
  const id = getValue("animeId");
  if (!id) {
    setStatus("Please enter an Anime ID first.", "error");
    showEmpty("Enter an Anime ID, then click View This Anime's Genres.");
    return;
  }
  return callApi(`/anime/${id}/genres`, {}, `Showing genres for anime ID ${id}.`, "animeGenres");
}

function getAllStudios() {
  return callApi("/studios", {}, "Showing all studios.", "studiosList");
}

function getStudioById() {
  const id = getValue("studioId");
  if (!id) {
    setStatus("Please enter a Studio ID first.", "error");
    showEmpty("Enter a Studio ID, then click Find Studio.");
    return;
  }
  return callApi(`/studios/${id}`, {}, `Showing studio with ID ${id}.`, "studioSingle");
}

function getAllGenres() {
  return callApi("/genres", {}, "Showing all genres.", "genresList");
}

function getGenreById() {
  const id = getValue("genreId");
  if (!id) {
    setStatus("Please enter a Genre ID first.", "error");
    showEmpty("Enter a Genre ID, then click Find Genre.");
    return;
  }
  return callApi(`/genres/${id}`, {}, `Showing genre with ID ${id}.`, "genreSingle");
}

function getAnimeForGenre() {
  const id = getValue("genreId");
  if (!id) {
    setStatus("Please enter a Genre ID first.", "error");
    showEmpty("Enter a Genre ID, then click View Anime in Genre.");
    return;
  }
  return callApi(`/genres/${id}/anime`, {}, `Showing anime for genre ID ${id}.`, "genreAnimeList");
}

async function createAnime() {
  const title = getValue("newTitle");
  const release_year = getValue("newYear");
  const episodes = getValue("newEpisodes");
  const studio_id = getValue("newStudioId");

  if (!title || !release_year || !episodes || !studio_id) {
    setStatus("Please fill in all fields before adding an anime.", "error");
    showEmpty("To add a new anime, fill in title, release year, episodes, and studio ID.");
    return;
  }

  const body = await callApi(
    "/anime",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        release_year: Number(release_year),
        episodes: Number(episodes),
        studio_id: Number(studio_id)
      })
    },
    `Anime "${title}" was added successfully.`,
    "animeSingle"
  );

  if (body !== null) {
    document.getElementById("newTitle").value = "";
    document.getElementById("newYear").value = "";
    document.getElementById("newEpisodes").value = "";
    document.getElementById("newStudioId").value = "";
  }
}

function fillCreateExample() {
  document.getElementById("newTitle").value = "Sample Anime";
  document.getElementById("newYear").value = "2024";
  document.getElementById("newEpisodes").value = "12";
  document.getElementById("newStudioId").value = "1";
  setStatus("Example values were added. You can change them before submitting.", "info");
}

async function updateAnime() {
  const anime_id = getValue("updateAnimeId");
  const title = getValue("updateTitle");
  const release_year = getValue("updateYear");
  const episodes = getValue("updateEpisodes");
  const studio_id = getValue("updateStudioId");

  if (!anime_id || !title || !release_year || !episodes || !studio_id) {
    setStatus("Please fill in every update field before saving changes.", "error");
    showEmpty("To update an anime, enter the anime ID and all new values.");
    return;
  }

  const body = await callApi(
    `/anime/${anime_id}`,
    {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        release_year: Number(release_year),
        episodes: Number(episodes),
        studio_id: Number(studio_id)
      })
    },
    `Anime ID ${anime_id} was updated successfully.`,
    "animeSingle"
  );

  if (body !== null) {
    document.getElementById("updateAnimeId").value = "";
    document.getElementById("updateTitle").value = "";
    document.getElementById("updateYear").value = "";
    document.getElementById("updateEpisodes").value = "";
    document.getElementById("updateStudioId").value = "";
  }
}

async function deleteAnime() {
  const anime_id = getValue("deleteAnimeId");

  if (!anime_id) {
    setStatus("Please enter an Anime ID before deleting.", "error");
    showEmpty("Enter an Anime ID, then click Delete Anime.");
    return;
  }

  const confirmed = window.confirm(`Are you sure you want to permanently delete anime ID ${anime_id}?`);
  if (!confirmed) {
    setStatus("Delete canceled.", "info");
    return;
  }

  const body = await callApi(
    `/anime/${anime_id}`,
    {
      method: "DELETE"
    },
    `Anime ID ${anime_id} was deleted successfully.`
  );

  if (body !== null) {
    document.getElementById("deleteAnimeId").value = "";
    renderMessageCard("Delete Complete", `Anime ID ${anime_id} was removed from the database.`);
  }
}