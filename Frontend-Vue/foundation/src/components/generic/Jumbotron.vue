<template>
  <b-jumbotron bg-variant="dark" text-variant="white" border-variant="dark" header-level="3" fluid tag="h4">
  <template slot="header">{{header}}</template>
  <p>
    {{description}}
  </p>
  </b-jumbotron>
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
