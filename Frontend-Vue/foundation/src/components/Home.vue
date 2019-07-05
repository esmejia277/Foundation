<template lang="html">
  <div id="Home">
    <div class="header-home"></div>
    <b-container fluid>
      <b-row class="about-us text-center text-justify bg-dark">
        <b-col>
          <h2 class="mb-5">
              <b-badge variant="light" >¿Quiénes somos?</b-badge>
          </h2>
          <p>La fundación el Resplandor de tu Gloria es una institución sin ánimo
            de lucro, que tiene como objetivo servir a las personas necesitadas de
            la ciudad de Medellín. Atendemos niños y familias de escasos recursos,
            brindándoles ayuda a sus necesidades básicas alimenticias, espirituales,
            psicológicas, educativas, vestuario, entre otros. Transformamos las vidas
            y los sueños de estas familias vulnerables con el amor de Jesús.</p>
        </b-col>
      </b-row>
      <b-row class="about-mission text-center text-justify bg-light">
        <b-col cols="4">
          <h2 class="mb-5">
              <b-badge variant="dark" >Misión</b-badge>
          </h2>
          <p>
            Es nuestra misión como fundación brindar las ayudas necesarias a los niños y
            familias en general por medio de nuestros programas de capacitación para el trabajo,
            la alimentación, asistencia psicológica y espiritual. Con el fin de mejorar
            su calidad de vida.
          </p>
        </b-col>
        <b-col cols="4">
          <h2 class="mb-5">
              <b-badge variant="dark" >Visión</b-badge>
          </h2>
          <p>
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
          <p>
            Atender la población de escasos recursos, ubicadas en las zonas vulnerables
            del municipio de Medellín, a través de nuestros programas de rehabilitación,
            educación, nutrición, apoyo psicosocial y espiritual.
          </p>
        </b-col>
      </b-row>
      
      
    </b-container>
    
    
  </div>
  
</template>

<script>
export default {
  name: "Home",
}
</script>

<style lang="css" scoped>

.header-home{
    background-image: url('../assets/foundation.jpg');
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
  padding-top: 50px;
  padding-bottom: 50px;
}

.about-mission{
  color:black;
  padding-top: 50px;
  padding-bottom: 50px;
  
}

</style>
