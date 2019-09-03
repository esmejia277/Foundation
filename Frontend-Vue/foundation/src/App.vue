<template>
  <div id="app">
    <Navbar/>
    <router-view/>
    <Foot/>
  </div>
</template>

<script>
import Navbar from './components/generic/Navbar.vue';
import Foot from './components/generic/Foot.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Foot,
  }
}
</script>

<style>

body{
  font-family: 'Ubuntu mono', monospace;
  font-size: 1.2rem;
  margin-bottom: 70px;
}


</style>
