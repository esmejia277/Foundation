<template lang="html">
  <div id="Home">
    <div class="header-home"></div>
    <b-container fluid>
      <b-row class="about-us text-center bg-dark">
        <b-col>
          <h2 class="mb-5">
              <b-badge variant="light" >¿Quiénes somos?</b-badge>
          </h2>
          <p class="text-justify">La fundación el Resplandor de tu Gloria es una institución sin ánimo
            de lucro, que tiene como objetivo servir a las personas necesitadas de
            la ciudad de Medellín. Atendemos niños y familias de escasos recursos,
            brindándoles ayuda a sus necesidades básicas alimenticias, espirituales,
            psicológicas, educativas, vestuario, entre otros. Transformamos las vidas
            y los sueños de estas familias vulnerables con el amor de Jesús.</p>
        </b-col>
      </b-row>
      <b-row class="about-info text-center" style="background-color:#f2f2f2;">
        <b-col cols="4">
          <h2 class="mb-5">
              <b-badge variant="dark" >Misión</b-badge>
          </h2>
          <p class="text-justify">
            Es nuestra misión como fundación brindar las ayudas necesarias a los niños y
            familias en general por medio de nuestros programas de capacitación para el trabajo,
            la alimentación, asistencia psicológica y espiritual. Con el fin de mejorar
            su calidad de vida.
          </p>
        </b-col>
        <b-col cols="4">
          <!-- <img src="static/img/climb.png" alt="" style="width:30%; background-color:grey;" class="p-5 rounded-circle"> -->
          <h2 class="mb-5">
              <b-badge variant="dark" >Visión</b-badge>
          </h2>
          <p class="text-justify">
            La fundación el Resplandor de tu Gloria será una organización social,
            especializada en el desarrollo de programas y proyectos efectivos e
            innovadores que promueven la formación de niños y jóvenes, la rehabilitación
            y resocialización de habitantes de la calle, además de nuestros programas
            de apoyo y capacitación para mujeres cabeza de familia.
          </p>
        </b-col>
        <b-col cols="4">
          <h2 class="mb-5">
              <b-badge variant="dark" >Objeto social</b-badge>
          </h2>
          <p class="text-justify">
            Atender la población de escasos recursos, ubicadas en las zonas vulnerables
            del municipio de Medellín, a través de nuestros programas de rehabilitación,
            educación, nutrición, apoyo psicosocial y espiritual.
          </p>
        </b-col>
      </b-row>

      <b-row class="about-us text-center text-justify text-dark">
        <b-col style="">
          <h2 class="mb-5">
              <b-badge variant="dark" >Dian</b-badge>
          </h2>
          <p >Aquí puedes encontrar todos los documentos legales que nos constituyen
            como fundación ante los entes gubernamentales colombianos.</p>
            <b-row class="card-file">
              <b-col cols="3" class="mt-4">
                  <CardFile title="Acta N°1"  fileLocation="static/dian/acta2019.pdf"/>
              </b-col>
              <b-col cols="3" class="mt-4">
                  <CardFile title="Antecedentes Judiciales" fileLocation="static/dian/certificado_de_antecedentes.pdf"/>
              </b-col>
              <b-col cols="3" class="mt-4">
                  <CardFile title="Estatutos de la Fundación" fileLocation="static/dian/estatutos_fundacion.pdf"/>
              </b-col>
              <b-col cols="3" class="mt-4">
                  <CardFile title="Estados financieros" fileLocation="static/dian/estados_financieros.pdf"/>
              </b-col>
              <b-col cols="3" class="mt-4">
                  <CardFile title="Dictamen Financiero" fileLocation="static/dian/dictamen_de_revisor.pdf"/>
              </b-col>
              <b-col cols="3" class="mt-4">
                  <CardFile title="Industria y comercio" fileLocation="static/dian/certificado_de_industria_y_comercio.pdf"/>
              </b-col>
              <b-col cols="3" class="mt-4">
                  <CardFile title="Informe de gestión" fileLocation="static/dian/informe_de_gestion_2018.pdf"/>
              </b-col>
              <b-col cols="3" class="mt-4">
                  <CardFile title="Cumplimiento" fileLocation="static/dian/certificado_de_cumplimiento.pdf"/>
              </b-col>
            </b-row>
        </b-col>
      </b-row>
    </b-container>
  </div>
  
</template>

<script>

import CardFile from './generic/CardFile'

export default {
  name: "Home",
  components:{
    CardFile,
  }
}
</script>

<style lang="css" scoped>

.header-home{
    background-image: url('../assets/img/foundation.jpg');
    background-position: center;
    background-size: cover;
    min-height: 75%;
    background-repeat: no-repeat;
    padding: 20%;
    -webkit-filter: contrast(200%);
    filter: contrast(200%);
    filter: brightness(70%);
}

.about-us{
  color:white;
  padding: 50px 70px 70px 70px;
  
}

.about-info{
  color:black;
  padding: 50px 50px 70px 70px;
  
}

.card-file{
  padding: 0 70px 70px 70px;
}

</style>
