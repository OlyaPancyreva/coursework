<template>
  <div>
    <table class="table table-hover">
      <thead>
      <tr>
        <th scope="col">Имя</th>
        <th scope="col">Почта</th>
        <th scope="col">Номер телефона</th>
        <th scope="col">Статус</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in items" @click="changeStatus(item.id)">
        <td>{{item.name}}</td>
        <td>{{item.mail}}</td>
        <td>{{item.phone}}</td>
        <td>
          <b-form-select>
            <b-form-select-option :key="item.status.id">
              {{item.status.status}}
            </b-form-select-option>
          </b-form-select>
        </td>
      </tr>

      </tbody>
    </table>

  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "RequestList",
    data() {
      return {
        items: '',
        status_id:'',
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
          url: "http://127.0.0.1:8000/request/",
          methods: 'GET',
          success: (response) => {
            console.log(response);
            this.items = response;

          },
          error: (response) => {
            alert("Невозможно получить список заявок ");
            console.log(response)
          }
        })
      },
      changeStatus(id) {
        $.ajax({
          url: "http://127.0.0.1:8000/status/" + id + "/",
          methods: 'PUT',
          data: {
            status_id: this.status_id,
          },
          success: (response) => {
            console.log(response);
          },
          error: (response) => {
            alert("Ошибка в редактировании");
          }
        })

      }
    }
  }
</script>

<style scoped>

</style>
