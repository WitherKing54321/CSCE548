const API_BASE = "http://127.0.0.1:8000";

document.getElementById("baseUrl").textContent = API_BASE;

async function callApi(path, options = {}) {
  const out = document.getElementById("output");
  out.textContent = "Loading...";

  try {
    const res = await fetch(API_BASE + path, options);
    const text = await res.text();

    out.textContent =
      `${options.method || "GET"} ${path}\n\n` +
      `Status: ${res.status} ${res.statusText}\n\n` +
      `Body:\n${text}`;
  } catch (err) {
    out.textContent = `Error calling API: ${err}`;
  }
}

/* ========================= */
/* GET FUNCTIONS */
/* ========================= */

function getAllAnime() { return callApi("/anime"); }

function getAnimeById() {
  const id = document.getElementById("animeId").value;
  return callApi(`/anime/${id}`);
}

function getGenresForAnime() {
  const id = document.getElementById("animeId").value;
  return callApi(`/anime/${id}/genres`);
}

function getAllStudios() { return callApi("/studios"); }

function getStudioById() {
  const id = document.getElementById("studioId").value;
  return callApi(`/studios/${id}`);
}

function getAllGenres() { return callApi("/genres"); }

function getGenreById() {
  const id = document.getElementById("genreId").value;
  return callApi(`/genres/${id}`);
}

function getAnimeForGenre() {
  const id = document.getElementById("genreId").value;
  return callApi(`/genres/${id}/anime`);
}

/* ========================= */
/* POST */
/* ========================= */

function createAnime() {
  const title = document.getElementById("newTitle").value;
  const release_year = document.getElementById("newYear").value;
  const episodes = document.getElementById("newEpisodes").value;
  const studio_id = document.getElementById("newStudioId").value;

  return callApi("/anime", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title,
      release_year,
      episodes,
      studio_id
    })
  });
}

/* ========================= */
/* PUT */
/* ========================= */

function updateAnime() {
  const anime_id = document.getElementById("updateAnimeId").value;
  const title = document.getElementById("updateTitle").value;
  const release_year = document.getElementById("updateYear").value;
  const episodes = document.getElementById("updateEpisodes").value;
  const studio_id = document.getElementById("updateStudioId").value;

  return callApi(`/anime/${anime_id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title,
      release_year,
      episodes,
      studio_id
    })
  });
}

/* ========================= */
/* DELETE */
/* ========================= */

function deleteAnime() {
  const anime_id = document.getElementById("deleteAnimeId").value;

  return callApi(`/anime/${anime_id}`, {
    method: "DELETE"
  });
}