<template lang="html">
  <b-card
    border-variant="dark"
    :header="title"
    header-text-variant="dark"
    align="center"
    style="font-size:1rem;"
    >
    <b-button variant="outline-success" pill :href="fileLocation" style="width:50%; font-size:0.6rem;" target="__blank">Ver</b-button>
  </b-card>
  
</template>

<script>
export default {
  name: 'CardFile',
  props:[
    'title',
    'fileLocation'
  ]
}
</script>