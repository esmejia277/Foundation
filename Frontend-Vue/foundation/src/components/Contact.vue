<template lang="html">
  
<div id="contact">
  <jumbotron class="text-justify" header="Contáctanos" description="Puedes escribirnos un mensaje acerca de nuestro trabajo;
  poner dudas, sugerencias e inquietudes."/>
  
<b-container class="p-4">
  <b-row align-h="center">
    <b-col cols="12" md="6" lg="6">
  <b-form @submit="sendForm">
    <b-form-group id="input-group-name" label="Tu nombre:" label-for="input-name">
      <b-form-input id="input-name"
        v-model="form.name"
        placeholder="Ingresa tu nombre"
        @blur="$v.form.name.$touch()">
      </b-form-input>
      <template v-if="$v.form.name.$error">
        <b-alert v-if="!$v.form.name.required" show variant="warning">Este campo es requerido</b-alert>
        <b-alert v-if="!$v.form.name.minLength" show variant="warning">Debes escribir al menos tres carácteres</b-alert>
      </template>
    </b-form-group>
    
  <b-form-group
    id="input-group-email"
    label="Correo electrónico:"
    label-for="input-email">
    <b-form-input
      id="input-email"
      v-model="form.email"
      type="email"
      placeholder="Ingresa tu correo electrónico"
      @blur="$v.form.email.$touch()">
      </b-form-input>
      <template v-if="$v.form.email.$error">
        <b-alert v-if="!$v.form.email.required" show variant="warning">Este campo es requerido</b-alert>
        <b-alert v-if="!$v.form.email.email" show variant="warning">Esta no es una dirección de correo correcta</b-alert>
      </template>
  </b-form-group>

  <b-form-group id="input-group-phone" label="Tu celular:"
  label-for="input-phone">
    <b-form-input id="input-phone"
      v-model="form.phone_number"
      placeholder="Ingresa tu número de celular"
      @blur="$v.form.phone_number.$touch()">
      </b-form-input>
      <template v-if="$v.form.phone_number.$error">
        <b-alert v-if="!$v.form.phone_number.required" show variant="warning">Este campo es requerido</b-alert>
        <b-alert v-if="!$v.form.phone_number.minLength" show variant="warning">Ingresa un número válido</b-alert>
        <b-alert v-if="!$v.form.phone_number.numeric" show variant="warning">Solo es posible ingresar números</b-alert>
        
      </template>
  </b-form-group>

  <b-form-group id="input-group-3" label="Mensaje:" label-for="input-message">
    <b-form-textarea
      id="textarea"
      v-model="form.message"
      placeholder="Déjanos un mensaje"
      rows="3"
      max-rows="6"
      @blur="$v.form.message.$touch()">
    </b-form-textarea>
    <template v-if="$v.form.message.$error">
      <b-alert v-if="!$v.form.message.required" show variant="warning">Este campo es requerido</b-alert>
      <b-alert v-if="!$v.form.message.minLength" show variant="warning">Debes escribir al menos treinta caracteres</b-alert>
    </template>
  </b-form-group>
  
  <b-button type="submit" variant="primary" >Enviar</b-button>
  <b-button variant="warning" @click="cleanForm()" >Limpiar</b-button>
  
</b-form>
  </b-col>

<b-col class="m-5" cols="12" md="6" lg="4">
  <b-card
    tag="article"
    style="max-width: 100%; border-radius: 30px;"
    class="mb-2"
  >
    <b-card-text>
        <p>
    <strong>Dirección</strong>
  </p>

  <p>Carrera 51 #54-12 Itagüí Colombia.</p>
  
  <p>
    <strong>Teléfono</strong>
  </p>
  <p>321 615 6158</p>
  
  <p>
    <strong>Correo electrónico</strong>
  </p>
  <p>resplandorsocial@gmail.com</p>
  
  <p>
    <strong>Redes sociales</strong>
  </p>
  
  <a href="https://www.facebook.com/Fundacion-El-Resplandor-de-tu-Gloria-172955893347063/" target="__blank">
   <i class="fab fa-facebook-square"></i>
 </a>
 <a href="https://www.instagram.com/elresplandordetugloria/?hl=en" target="__blank">
   <i class="fab fa-instagram"></i>
 </a>
    </b-card-text>
  </b-card>



	</b-col>
</b-row>
</b-container>
</div>
</template>

<script>
import {
  required,
  minLength,
  email,
  between,
  numeric,
} from 'vuelidate/lib/validators'

import Jumbotron from './generic/Jumbotron'

export default {
  name: 'Contact',
  components: {
    Jumbotron
  },
  data() {
    return {
      form: {
        name: '',
        email: '',
        phone_number: '',
        message: '',
      },
    }
  },
  validations: {
    form: {
      name: {
        required,
        minLength: minLength(3),

      },
      email: {
        required,
        email
      },
      phone_number: {
        required,
        numeric,
        minLength: minLength(10)


      },
      message: {
        required,
        minLength: minLength(30),
      }
    }
  },
  methods: {
    sendForm() {
      this.$v.form.$touch()
      if (this.$v.form.$invalid) {
        return
      }
      this.axios.post('http://127.0.0.1:8000/api/v1/contact/insert', this.form)
        .then((response) => {
          if (response.statusText === 'Created') {
            this.$alertify.alert('Éxitoso', '¡Tus datos han sido enviados correctamente!');
            this.$router.push('/');
          }
        }).catch((error) => {
          this.$alertify.error('Oops! Ha ocurrido un problema con el envío de tus datos, por favor intentalo de nuevo.');
        });
    },
    cleanForm() {
      this.form.name = '';
      this.form.email = '';
      this.form.phone_number = '';
      this.form.message = '';
    }
  }
}
</script>

<style lang="css" scoped>

/* #contact{
  margin-bottom: 90px;
} */

.alert{
  font-size: 15px !important;
  font-weight: bold;
  margin-top: 12px;
}

i{
  font-size: 45px;
  margin-top: 7px;
  color:black;
}

i:hover{
  color:grey;
}

p {
  font-size: 1.2rem;
}

</style>
