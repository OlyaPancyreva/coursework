<template>
  <table class="table table-hover">
    <thead>
    <tr>
      <th scope="col">Кем забронировано</th>
      <th scope="col">Страна назначения</th>
      <th scope="col">Город вылета</th>
      <th scope="col">Дата вылета</th>
      <th scope="col">Отель</th>
      <th scope="col">email клиента</th>
      <th scope="col">Статус</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="item in items">
      <td>{{item.user.username}}</td>
      <td>{{item.tour.destinationCountry}}</td>
      <td>{{item.tour.departure}}</td>
      <td>{{item.tour.date}}</td>
      <td>{{item.tour.hotel.name}}, {{item.tour.hotel.city}} {{item.tour.hotel.rating}}*<br>
        ({{item.tour.mealType.name}})
      </td>
      <td>{{item.user.email}}</td>
      <td>
          <b-form-select  style="min-width: 200px">
            <b-form-select-option>
              {{item.status.status}}
            </b-form-select-option>
          </b-form-select>
        </td>
    </tr>

    </tbody>
  </table>
</template>

<script>
  import $ from "jquery";

  export default {
    name: "SoldTour",
    data() {
      return {
        items: '',
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
      this.uploadList();
    },
    methods: {
      uploadList() {
        $.ajax({
          url: "http://127.0.0.1:8000/sold/",
          methods: 'GET',
          success: (response) => {
            console.log(response);
            this.items = response;

          },
          error: (response) => {
            alert("Невозможно получить бронирования ");
            console.log(response)
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
