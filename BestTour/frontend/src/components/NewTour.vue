<template>
  <div>
    <form style="max-width: 500px">
      <label for="destCountry">Страна назначения:</label>
      <input type="text" class="form-control" id="destCountry" v-model="destinationCountry">
      <label for="city">Город отправления:</label>
      <input type="text" class="form-control" id="city" v-model="departure">
      <label for="hotel">Отель:</label>
      <select id="hotel" class="form-control">
        <option v-for="hotel in hotels" :key="hotel.id">
          {{hotel.city}}, {{hotel.name}}
          {{hotel.rating}}*
        </option>
      </select>
      <label for="meal">Тип питания:</label>
      <select id="meal" class="form-control">
        <option v-for="meal in typeMeal" :key="meal.id">
          {{meal.name}}
        </option>
      </select>
      <label for="count">Количество ночей:</label>
      <input type="number" class="form-control" id="count" v-model="dayCount">
      <label for="date">Дата вылета:</label>
      <input id="date" class="form-control" type="date" v-model="date">

      <label for="description">Описание</label>
      <textarea class="form-control" id="description" v-model="description"></textarea>
      <label for="price">Цена:</label>
      <input id="price" class="form-control" type="number" v-model="price">

      <input id="hottour" type="checkbox" class="form-check-input" style="margin: 10px; margin-top: 15px"
             v-model="HotTour">
      <label for="hottour" style="margin-left: 30px;margin-top: 10px">Горящий тур</label>
<!--      <b-form-file class="mt-3" plain></b-form-file>-->

      <button type="button" class="btn btn-primary" style="margin-top: 20px" @click="setTour()">Сохранить</button>

    </form>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "NewTour",
    data() {
      return {
        hotels: '',
        typeMeal: '',
        destinationCountry: '',
        departure: '',
        hotelId: '',
        mealType: '',
        date: '',
        dayCount: '',
        description: '',
        price: '',
        HotTour: '',
        image: '',
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
      this.getHotel();
      this.getMealType();
    },
    methods: {
      getHotel() {
        $.ajax({
          url: "http://127.0.0.1:8000/hotel/",
          type: 'GET',
          success: (response) => {
            console.log(response);
            this.hotels = response;

          },
          error: (response) => {
            console.log(response)
          }
        });
      },
      getMealType() {
        $.ajax({
          url: "http://127.0.0.1:8000/meal/",
          type: 'GET',
          success: (response) => {
            console.log(response);
            this.typeMeal = response;

          },
          error: (response) => {
            console.log(response)
          }
        });
      },
      setTour() {
        $.ajax({
          url: "http://127.0.0.1:8000/tour/create/",
          type: 'POST',
          data: {
            destinationCountry: this.destinationCountry,
            departure: this.departure,
            hotel: this.hotelId,
            mealType: this.mealType,
            date: this.date,
            dayCount: this.dayCount,
            description: this.description,
            price: this.price,
            HotTour: this.HotTour,
            image: this.image,
          },
          success: (response) => {
            alert("Тур успешно добавлен");
            this.$router.push({name: "home"})
            console.log(response);
          },
          error: (response) => {
            alert("Вы ввели неккоректные данные");
            console.log(response)
          }
        });
      }
    }
  }
</script>

<style scoped>
</style>
