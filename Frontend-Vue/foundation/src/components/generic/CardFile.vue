<template lang="html">
  <b-card
    border-variant="dark"
    :header="title"
    header-text-variant="dark"
    align="center"
    >
    <b-card-img src="static/img/pdf.png" style="width:120px;"></b-card-img>
    
    <b-button variant="outline-success" pill :href="fileLocation" target="__blank">Vizualizar</b-button>
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

<style lang="css" scoped>
</style>
