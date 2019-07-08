<template>
<div id="navbar">
  <b-navbar toggleable="md" type="dark" variant="dark" class="navbar-color">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-navbar-brand>
      <router-link to="/" class="navbar-logo">
        <img id="logo" src="../../assets/img/white_logo.png" width="80px;" alt="Logo de la fundación">
      </router-link>
    </b-navbar-brand>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav class="ml-auto">
        <b-nav-item>
          <router-link to="/" class="nav-link">
            <i class="fas fa-home"></i>
            Inicio
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <b-nav-item-dropdown class="programs" text="Programas">
            <b-dropdown-item class="links">
              <router-link to="/programas/haciendo-amigos" class="dropdown-link">
                <i class="far fa-heart"></i>
                Haciengo Amigos
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item href="#">
              <router-link to="/programas/proyecto-colegios/" class="dropdown-link">
                <i class="fas fa-pen"></i>
                Proyecto Colegios
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item href="#">
              <router-link to="/programas/talleres-de-aprendizaje" class="dropdown-link">
                <i class="fas fa-cut"></i>
                Talleres de aprendizaje
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item class="links">
              <router-link to="/programas/plan-padrino" class="dropdown-link">
                <i class="fas fa-child"></i>
                Plan padrino
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item class="links">
              <router-link to="/programas/familias" class="dropdown-link">
                <i class="fas fa-users"></i>
                Apoyo a familias
              </router-link>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-nav-item>
        <b-nav-item>
          <router-link to="/documentos-legales" class="nav-link">
            <i class='fas fa-university'></i>
            DIAN
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link to="/Contactanos" class="nav-link">
            <i class="far fa-paper-plane"></i>
            Contáctanos
          </router-link>
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>

.nav-link {
  font-size: 20px;
}

.dropdown-link {
  color: black;
  text-decoration: none;
  font-size: 20px;
}
</style>
