<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/generic/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
  }
}
</script>

<style>

body{
  font-family: 'Ubuntu mono', monospace;
  font-size: 1.5rem;
  
}

</style>
