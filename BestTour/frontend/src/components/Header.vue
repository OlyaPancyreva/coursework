<template>
  <div>
    <!--    Шапка сайта-->
    <div
      class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-1 bg-white border-bottom shadow-sm my-header">
      <a class="my-0 mr-md-auto text-info" href="#"></a>
      <nav class="my-2 my-md-0 mr-md-3" style="text-align: right">
        <a class="my-0 mr-md-auto text-info" href="#" @click="adminPage" v-show="isAdmin">Страница
          администратора</a>
        <a class="p-3 text-dark" @click="mainPage" href="#">Главная</a>
        <a class="p-3 text-dark" @click="allTour" href="#">Все туры</a>
        <a class="p-3 text-dark" @click="hotTour" href="#">Горящие туры</a>
        <a v-b-modal.modal-2 class="p-3 text-dark" href="#" v-show="!get_auth">Регистрация</a>
      </nav>
      <a v-b-modal.modal-1 class="btn btn-outline-primary" v-show="!get_auth">Вход</a>
      <a class="btn btn-outline-primary" v-show="get_auth" @click="personalArea" style="margin-right: 20px">Личный
        кабинет</a>
      <a class="btn btn-outline-primary" v-show="get_auth" @click="logout">Выход</a>
    </div>
    <!--    Конец шапки сайта-->
    <!--    модальное окно для авторизации    -->
    <b-modal id="modal-1" title="Авторизация" @ok="auth">
      <b-form-group
        id="login"
        label="Логин"
        label-for="login"
      >
        <b-form-input
          v-model="login"
          id="login"
          type="email"
          required
          placeholder="Введите логин"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        id="password"
        label="Пароль"
        label-for="password"
      >
        <b-form-input
          v-model="password"
          id="password"
          type="password"
          required
          placeholder="Введите пароль"
        ></b-form-input>
      </b-form-group>
    </b-modal>

    <!--    модальное окно для регистрации  -->
    <b-modal id="modal-2" title="Регистрация" @ok="registration">
      <b-form-group
        id="login-reg"
        label="Логин"
        label-for="login-reg"
        description="Только буквы, цифры и символы @/./+/-/_"
      >
        <b-form-input
          v-model="login_reg"
          id="login-reg"
          type="text"
          required
          placeholder="Введите логин"
        >
        </b-form-input>
      </b-form-group>
      <b-form-group
        id="email-reg"
        label="Email"
        label-for="email-reg">
        <b-form-input
          v-model="email_reg"
          id="email-reg"
          type="email"
          required
          placeholder="Введите email"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        id="password-reg"
        label="Пароль"
        label-for="password-reg"
        description="Пароль должен содержать не менее 8 символов"
      >
        <b-form-input
          v-model="password_reg"
          id="password-reg"
          type="password"
          required
          placeholder="Введите пароль"
        ></b-form-input>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "Header",
  data() {
    return {
      login: '',
      password: '',
      login_reg: '',
      password_reg: '',
      email_reg: '',
      get_auth: '',
      isAdmin: '',
    }
  },
  methods: {
    auth(bvModalEvt) {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/login/",
        type: "POST",
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          alert("Вы авторизированы");
          sessionStorage.setItem("auth_token", response.auth_token);
          this.isAdmin = this.login === 'admin';
          sessionStorage.setItem("admin", this.isAdmin);
          sessionStorage.setItem("username", this.login);
          this.get_auth = true;
        },
        error: (response) => {
          if (response.status === 400) {
            alert("Неверный логин или пароль");
          }
          console.log(response)
        }
      })
    },
    registration(bvModalEvt) {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/",
        type: "POST",
        data: {
          username: this.login_reg,
          password: this.password_reg,
          email: this.email_reg,
        },
        success: (response) => {
          if (response.status === 201) {
            alert("Вы успешно зарегистрировались")
          }
        },
        error: (response) => {
          if (response.status === 400) {
            alert("Неверно заполнены поля");
          }
          console.log(response)
        }
      })
    },
    check_auth() {
      this.get_auth = sessionStorage.getItem("auth_token") !== null;
      this.isAdmin = sessionStorage.getItem("admin");
    },
    logout() {
      this.get_auth = false;
      sessionStorage.removeItem("auth_token");
      sessionStorage.removeItem("admin");
      sessionStorage.removeItem("username");
      this.isAdmin = false;
      this.mainPage()
    },
    personalArea() {
      this.$router.push({name: "personalArea"})
    },
    mainPage() {
      this.$router.push({name: "home"})
    },
    adminPage() {
      this.$router.push({name: "adminPage"})
    },
    allTour() {
      this.$router.push({name: "allTour"})
    },
    hotTour() {
      this.$router.push({name: "hotTour"})
    },
  },
  created() {
    this.check_auth()
  }
}
</script>


<style scoped>
.my-header {
  position: fixed;
  width: 100%;
  z-index: 1;
}
</style>
