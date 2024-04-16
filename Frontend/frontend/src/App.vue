<!-- eslint-disable prettier/prettier -->
<template>
  <div id="app">
    <header>
      <h1>What's your Sign?</h1>
    </header>
    <HomeView/>
  </div>
</template>

<!-- eslint-disable prettier/prettier -->
<script>
import HomeView from './components/HomeView.vue'

export default {
  name: 'App',
  components: {
    HomeView
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #a0c5eb;
}

header {
  text-align: center;
  margin: 20px 0;
}

h1 {
  font-size: 3em;
  color: #000000;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  border: 1px solid #000000;
  border-radius: 5px;
  padding: 5px 10px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #a0c5eb;
  background-image: url("./assets/Horoscope.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  position: relative;
}

#app::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.75); /* Black overlay with 50% opacity */
  z-index: -1; /* Ensures the overlay is behind the content */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

.image-icon {
  max-width: 8em;
  margin-top: 2em;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
