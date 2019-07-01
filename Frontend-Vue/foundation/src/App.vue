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

*{
  font-family: 'Ubuntu mono', monospace;
}

</style>
