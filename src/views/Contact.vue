<template>
  <header>
    <router-view></router-view>

  </header>
  <div id="videos">
    <h1>Featured YouTube Videos</h1>
    <div class="video-grid">
      <iframe 
        v-for="(video, index) in videos" 
        :key="index"
        :src="`https://www.youtube.com/embed/${video}`" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
      </iframe>
    </div>
    
  </div>
</template>

<script>
export default {
  name: "VideoComponent",
  data() {
    return {
      videos: [
        "dQw4w9WgXcQ", // Replace these with your actual video IDs
        "3JZ_D3ELwOQ",
        "M7lc1UVf-VE",
        "K4TOrB7at0Y",
        "C0DPdy98e4c",
        "fRh_vgS2dFE"
      ]
    };
  }
};
</script>

<style scoped>
header {
  
}
.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1em;
  padding: 1em;
}

iframe {
  width: 100%;
  height: 200px;
}
</style>
