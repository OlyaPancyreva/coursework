<template>
  <div>
    <b-card class="my-card">
      <b-aspect :aspect="2">
        <b-card class="my-card2">
          <b-aspect :aspect="11">
            <p class="card-title" style="font-family: 'Lobster', cursive; text-align: center; font-size: 38px">Туристическая компания «Best Tour»</p>
            <Carousel></Carousel>
            <h3 style="margin: 30px">Новости</h3>
            <b-card-group deck
                          style="color: #0f6890; margin:10px;font-family: 'Open Sans', Helvetica, Arial, sans-serif;">
              <b-card>
                <b-card-text>ОБНОВЛЕНИЕ САЙТА</b-card-text>
                <b-card-text style="color: black; font-size: 14px">Мы постоянно развиваемся и рады представить Вам наш
                  новый сайт. Просто нажмите на кнопку "забронировать" и наш менеджер Вам перезвонит.
                </b-card-text>
              </b-card>
              <b-card>
                <b-card-text>АДАПТИВНЫЙ САЙТ</b-card-text>
                <b-card-text style="color: black; font-size: 14px">Наш сайт адаптирован для мобильных устройств, а это
                  значит, что Вы можете искать обычные туры
                  или просматривать горящие путевки прямо со своего телефона или планшета.
                </b-card-text>
              </b-card>
              <b-card>
                <b-card-text>ОНЛАЙН ПОИСК ТУРОВ 24/7</b-card-text>
                <b-card-text style="color: black; font-size: 14px">Мы используем передовые технологии в туризме, а это
                  значит, что на нашем сайте Вы можете найти туры в режиме онлайн, в любое время суток.
                </b-card-text>
              </b-card>
            </b-card-group>
            <img src="../assets/page.png" alt="..."
                 style="width: 910px; height: auto; margin-left: 24px; margin-right: auto; margin-bottom: 40px">
            <div class="container" style="margin: 30px; ">
              <div class="row">
                <div class="col-1-2">
                  <h4>Не смогли подобрать подходящий тур?</h4>
                  <p class="text-muted">Оставьте заявку, и мы найдем то, что Вам нужно. Мы отвечаем быстро, не рассылаем
                    спам и не навязываем дополнительных услуг. Просто попробуйте и убедитесь сами!</p>
                </div>
                <div class="col-1-2">
                  <b-button v-b-modal.modal-sm class="btn-req">Оставить заявку на тур</b-button>
                  <b-modal id="modal-sm" size="sm" title="Оставьте заявку на тур" ref="modal" @ok="handleOk">
                    <b-form-group>
                      <b-form-input id="name" v-model="name" placeholder="Введите свое имя" class="mrgn"></b-form-input>
                      <b-form-input id="mail" v-model="mail" placeholder="Введите почту" class="mrgn"></b-form-input>
                      <b-form-input id="phone" type="tel" v-model="phone" placeholder="Номер телефона"
                                    class="mrgn"></b-form-input>
                    </b-form-group>
                  </b-modal>
                </div>
              </div>
            </div>
          </b-aspect>
        </b-card>

      </b-aspect>
      <Footer></Footer>
    </b-card>
  </div>
</template>
<script>
  import Header from "./Header";
  import Carousel from "./Carousel";
  import Footer from "./Footer";
  import $ from 'jquery'

  export default {
    name: "Home",
    components: {Footer, Carousel, Header},
    data() {
      return {
        name: '',
        mail: '',
        phone: '',
      }
    },
    methods: {
      checkFormValidity() {
        const valid = this.$refs.form.checkValidity();
        this.nameState = valid;
        return valid
      },
      handleOk(bvModalEvt) {
        $.ajax({
          url: "http://127.0.0.1:8000/request/",
          type: "POST",
          data: {
            name: this.name,
            mail: this.mail,
            phone: this.phone,
          },
          success: (response) => {
            alert("Заявка зарегистрирована")
          },
          error: (response) => {
            alert("Были введены некорректные данные");
            console.log(response)
          }
        })
      },
      handleSubmit() {
        if (!this.checkFormValidity()) {
          return
        }
        this.$nextTick(() => {
          this.$bvModal.hide('modal-prevent-closing')
        })
      }
    }
  }
</script>

<style scoped>
  .img {
    width: 60%;
    margin-right: auto;
    margin-left: auto;
  }

  .col-1-2 {
    width: 50%;
    float: left;
  }

  .btn-req {
    margin-left: 20%;
    margin-top: 8%;
    min-height: 50px;
    width: auto;
    font-size: 20px;
    background-color: #ff9900 !important;
    display: flex;
    animation: radial-pulse 1s infinite;
  }

  @keyframes radial-pulse {
    0% {
      box-shadow: 0 0 0 0px rgba(0, 0, 0, 0.5);
    }

    100% {
      box-shadow: 0 0 0 40px rgba(0, 0, 0, 0);
    }
  }

  .mrgn {
    margin: 10px;
    width: 250px;
    margin-top: 20px;
  }
</style>
