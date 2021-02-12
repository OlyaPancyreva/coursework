<template>
  <b-card class="my-card">
    <b-aspect :aspect="2">
      <b-card class="my-card2">
        <b-aspect :aspect="11">
          <div class="main">
            <div class="container">
              <div class="row">
                <div class="col-1-3">
                    <img src="../assets/olik.png" class="avatar" alt="">
                </div>
                <div class="col-2-3">
                  <p style="font-size: 20px">
                    Имя: {{username}}
                  <br>
                  e-mail: {{tours[6].user.email}}
                  </p>
                </div>
              </div>
              <div class="row">
                <div class="col-1-2"></div>
                <div class="col-1-2"></div>
              </div>
              <div class="row">
                <div class="col-1-4"></div>
                <div class="col-1-4"></div>
                <div class="col-1-2"></div>
              </div>
            </div>
          </div>
          <div v-for="t in tours">
            <div v-if="username===t.user.username">
              <div v-if="new Date(t.tour.date)> new Date()">
                <div class="card mb-3"
                     style="max-width: 760px; min-height:230px; margin-left: auto; margin-right: auto">
                  <div class="row no-gutters">
                    <div class="col-md-4">
                      <img :src="'http://127.0.0.1:8000'+t.tour.image"
                           style="margin:15px; max-height: 175px; width: auto;" alt="...">
                    </div>
                    <div class="col-md-8">
                      <div class="card-body">
                        <h4 class="card-title">{{ t.tour.destinationCountry }}</h4>
                        <p class="card-text">
                        <div>{{ t.tour.hotel.name }}, {{ t.tour.hotel.city }} {{ t.tour.hotel.rating }}*
                          ({{ t.tour.hotel.roomType.name }}, {{ t.tour.mealType.name }})
                        </div>
                        <div>Город вылета: {{ t.tour.departure }}</div>
                        <div>Дата вылета: {{ t.tour.date }}</div>
                        <div>Количество ночей: {{ t.tour.dayCount }}</div>
                        <p class="card-text"><small class="text-muted">{{ t.tour.description }}</small></p>
                        <h4>{{ t.tour.price }} руб/чел.
                        </h4>
                      </div>
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
  name: "PersonalArea",
  data() {
    return {
      tours: '',
      username: '',
    }
  },
  created() {
    if (sessionStorage.getItem("username") !== null) {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
    }
    this.getTour();
    this.username = sessionStorage.getItem("username")
  },
  methods: {
    getTour() {
      $.ajax({
        url: "http://127.0.0.1:8000/booked/",
        methods: 'GET',
        success: (response) => {
          console.log(response);
          this.tours = response;

        },
        error: (response) => {
          alert("Error");
          console.log(response)
        }
      });
    }
  }
}
</script>

<style scoped>
.col-1-2 {
  width: 50%;
  float: left;
}
.col-1-3 {
  width: 20%;
  float: left;
  margin-left: 50px;
}
.col-1-4 {
  width: 25%;
  float: left;
}
.col-2-3 {
  margin-top: 50px;
  width: 66.6666666667%;
  float: left;
}
.container:after, .row:after {
  content: "";
  display: table;
  clear: both;
}
.row {
  margin-bottom: 15px;
}

.avatar {
  margin: 50px;
  width: 100px;
  border: 3px solid #000000;
  padding: 5px;
}
</style>
