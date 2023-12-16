// Remplacez 'YOUR_API_KEY' par votre propre clé API YouTube Data API v3
const apiKey = 'YOUR_API_KEY';

// Fonction pour récupérer les détails d'une vidéo par son ID
async function getVideoDetails(videoId) {
  const url = `https://www.googleapis.com/youtube/v3/videos?id=${videoId}&part=snippet,contentDetails&key=${apiKey}`;
  
  try {
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.items && data.items.length > 0) {
      const videoDetails = data.items[0];
      console.log('Video Details:', videoDetails);
      return videoDetails;
    } else {
      console.error('Video not found.');
      return null;
    }
  } catch (error) {
  console.error('Error fetching video details:', error);
    return null;
  }
}

// Fonction pour rechercher des vidéos par mot-clé
async function searchVideosByKeyword(keyword) {
  const url = `https://www.googleapis.com/youtube/v3/search?q=${keyword}&part=snippet&key=${apiKey}`;
  
  try {
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.items && data.items.length > 0) {
      const videos = data.items;
      console.log('Search Results:', videos);
      return videos;
    } else {
      console.error('No videos found for the keyword.');
      return [];
    }
  } catch (error) {
    console.error('Error searching videos:', error);
    return [];
  }
}

// Exemple d'utilisation des fonctions
const videoId = 'VIDEO_ID'; // Remplacez par l'ID d'une vidéo YouTube
getVideoDetails(videoId);

const searchKeyword = 'JavaScript Tutorial'; // Remplacez par le mot-clé de recherche
searchVideosByKeyword(searchKeyword);
