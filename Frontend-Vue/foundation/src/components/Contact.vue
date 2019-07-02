<template lang="html">
  
<div id="contact">
  <b-jumbotron bg-variant="dark" text-variant="white" border-variant="dark" header-level="3" fluid tag="h4">
    <template slot="header">Contáctanos</template>
    <p>
      Puedes escribirnos un mensaje acerca de nuestro trabajo;
      puedes poner dudas, sugerencias, inquietudes.
    </p>
  </b-jumbotron>
  
<b-container class="mt-5">
  <b-form @submit="sendForm">
    <b-form-group id="input-group-name" label="Tu nombre:" label-for="input-name">
      <b-form-input id="input-name"
        v-model="form.name"
        placeholder="Ingresa tu nombre">
      </b-form-input>
    </b-form-group>
    
  <b-form-group
    id="input-group-email"
    label="Correo electrónico:"
    label-for="input-email">
    <b-form-input
      id="input-email"
      v-model="form.email"
      type="email"
      placeholder="Ingresa tu correo electrónico">
      </b-form-input>
  </b-form-group>


  <b-form-group id="input-group-phone" label="Tu celular:"
  label-for="input-phone"
  description="Ingresa el código de tu país, ejemplo (COLOMBIA +573192937849)">
    <b-form-input id="input-phone"
      v-model="form.phone_number"
      placeholder="Ingresa tu nombre">
      </b-form-input>
  </b-form-group>

  <b-form-group id="input-group-3" label="Mensaje:" label-for="input-message">
    <b-form-textarea
      id="textarea"
      v-model="form.message"
      placeholder="Déjanos un mensaje"
      rows="3"
      max-rows="6"
    ></b-form-textarea>
  </b-form-group>
  <b-button type="submit" variant="primary" >Enviar</b-button>
  <b-button variant="warning" @click="cleanForm()" >Limpiar</b-button>
</b-form>
</b-container>
</div>
</template>

<script>
export default {
  name: 'Contact',
  data() {
    return {
      form: {
        name: '',
        email: '',
        phone_number: '+57',
        message: '',
      },
    }
  },
  methods: {
    sendForm() {
      if(this.form.name.length !== 0 && this.form.email.length !== 0
        && this.form.phone_number.length !== 0 && this.form.message.length !== 0){
          this.axios.post('http://127.0.0.1:8000/api/v1/contact/insert', this.form)
            .then((response) => {
              if (response.statusText === 'Created') {
                this.$alertify.alert('Éxitoso', '¡Tus datos han sido enviados correctamente!');
              }
            }).catch((error) => {
              this.$alertify.error('Oops! Ha ocurrido un problema con el envío de tus datos, por favor intentalo de nuevo');
            });
        }else{
          this.$alertify.error('Por favor llena todos los campos');
        }
        
    },
    cleanForm(){
      this.form.name = '';
      this.form.email = '';
      this.form.phone_number = '+57';
      this.form.message = '';
    }
  }
}
</script>

<style lang="css" scoped>

#contact{
  margin-bottom: 90px;
}




</style>
