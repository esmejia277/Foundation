<template lang="html">
  
<div id="contact">
  <jumbotron header="Contáctanos" description="Puedes escribirnos un mensaje acerca de nuestro trabajo;
  puedes poner dudas, sugerencias, inquietudes."/>
  
<b-container class="mt-5">
  <b-form @submit="sendForm">
    <b-form-group id="input-group-name" label="Tu nombre:" label-for="input-name">
      <b-form-input id="input-name"
        v-model="form.name"
        placeholder="Ingresa tu nombre"
        @blur="$v.form.name.$touch()">
      </b-form-input>
      <template v-if="$v.form.name.$error">
        <b-alert v-if="!$v.form.name.required" dismissible show variant="warning">Este campo es requerido</b-alert>
        <b-alert v-if="!$v.form.name.minLength" dismissible show variant="warning">Debes escribir al menos tres carácteres</b-alert>
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
        <b-alert v-if="!$v.form.email.required" dismissible show variant="warning">Este campo es requerido</b-alert>
        <b-alert v-if="!$v.form.email.email" dismissible show variant="warning">Esta no es una dirección de correo correcta</b-alert>
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
        <b-alert v-if="!$v.form.phone_number.required" dismissible show variant="warning">Este campo es requerido</b-alert>
        <b-alert v-if="!$v.form.phone_number.minLength" dismissible show variant="warning">Ingresa un número válido</b-alert>
        <b-alert v-if="!$v.form.phone_number.numeric" dismissible show variant="warning">Solo es posible ingresar números</b-alert>
        
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
      <b-alert v-if="!$v.form.message.required" dismissible show variant="warning">Este campo es requerido</b-alert>
      <b-alert v-if="!$v.form.message.minLength" dismissible show variant="warning">Debes escribir al menos treinta caracteres</b-alert>
    </template>
  </b-form-group>
  
  <b-button type="submit" variant="primary" >Enviar</b-button>
  <b-button variant="warning" @click="cleanForm()" >Limpiar</b-button>
</b-form>
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

import jumbotron from './generic/Jumbotron'

export default {
  name: 'Contact',
  components:{
    jumbotron
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
            this.$router.push('Home');
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


</style>
