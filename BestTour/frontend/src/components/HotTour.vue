<template>
  <b-card class="my-card">
    <b-aspect :aspect="2">
      <b-card class="my-card2">
        <b-aspect :aspect="11">
          <div v-for="tour in tours">
            <div v-if="new Date(tour.date) > new Date()">
              <div class="card mb-3" style="max-width: 760px; min-height:230px; margin-left: auto; margin-right: auto">
                <div class="row no-gutters">
                  <div class="col-md-4">
                    <img :src="tour.image"
                         style="margin:15px; max-height: 175px; width: auto;" alt="...">
                  </div>
                  <div class="col-md-8">
                    <div class="card-body">
                      <h4 class="card-title">{{tour.destinationCountry}}</h4>
                      <p class="card-text">
                      <div>{{tour.hotel.name}}, {{tour.hotel.city}} {{tour.hotel.rating}}*
                        ({{tour.hotel.roomType.name}}, {{tour.mealType.name}})
                      </div>
                      <div>Город вылета: {{tour.departure}}</div>
                      <div>Дата вылета: {{tour.date}}</div>
                      <div>Количество ночей: {{tour.dayCount}}</div>
                      <p class="card-text"><small class="text-muted">{{tour.description}}</small></p>

                      <h4>{{tour.price}} руб/чел.
                        <b-button class="btn-r" pill variant="primary" @click="toBook(tour.id)">Забронировать</b-button>
                      </h4>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </b-aspect>
      </b-card>
    </b-aspect>
  </b-card>
</template>

<script>
  import $ from "jquery";

  export default {
    name: "HotTour",
    data() {
      return {
        tours: '',
      }
    },
    created() {
      if (sessionStorage.getItem("username") !== null) {
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
      }
      this.tourList();
    },
    methods: {
      tourList() {
        $.ajax({
          url: "http://127.0.0.1:8000/hottour/",
          methods: 'GET',
          success: (response) => {
            console.log(response);
            this.tours = response;
          },
          error: (response) => {
            alert("Не удалось загрузить список туров");
            console.log(response)
          }
        });
      },
      toBook(id) {
        if (sessionStorage.getItem("username") !== null) {
          $.ajax({
            url: "http://127.0.0.1:8000/booked/",
            type: "POST",
            data: {
              tour: id,
            },
            success: (response) => {
              alert("Вы забронировали тур");
              this.$router.push({name: "personalArea"})
              console.log(response)
            },
            error: (response) => {
              alert("Не удалось забронировать тур")
            }
          })
        } else alert("Для брони необходимо авторизоваться, либо зарегистрироваться")

      },
    }
  }
</script>

<style scoped>
</style>
