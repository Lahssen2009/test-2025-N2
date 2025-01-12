<template>
  <div>
    <h1>Welcome to my Vite + Vue App</h1>
    <p>
      This is a simple app that uses Vite to build and serve a Vue 3 application.
    </p>
    <p>
      To get started, edit <code>src/App.vue</code> and save to reload.
    </p>
    <main>
      <router-view></router-view>
    </main>
  </div>
  <footer>
    <router-link to="/">Home</router-link> | <router-link to="/about">About</router-link> | <router-link to="/contact">Contact</router-link>
    <p>&copy; 2023 My App. All rights reserved.</p>
  </footer>
</template>

<style scoped>
  h1 {
    font-size: 2em;
    text-align: center;
  }

  p {
    text-align: center;
  }
</style>
