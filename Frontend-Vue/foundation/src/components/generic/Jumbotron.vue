<template>
  <div id="Jumbotron">
    <b-jumbotron bg-variant="dark" text-variant="white" border-variant="dark" header-level="3" fluid tag="h4">
    <template slot="header">
      <h1 class="text-center">
        <strong>
        {{header}}
        </strong>
      </h1>
    </template>
    <p>
      {{description}}
    </p>
    </b-jumbotron>
  </div>
</template>

<script>

export default{
  nane: 'Jumbotron',
  props:[
    'header',
    'description'
  ]
}
</script>

<style scoped>
@media only screen and (max-width: 600px) {
  p {
    font-size: 1rem;
  }
}






</style>
