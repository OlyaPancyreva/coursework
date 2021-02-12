<template>
  <!--  <div>
      <table class="table table-hover">
        <thead>
        <tr>
          <th scope="col">Имя</th>
          <th scope="col">Почта клиента</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="item in items">
            <td>{{item.user.username}}</td>
            <td>{{item.user.email}}</td>
        </tr>

        </tbody>
      </table>
    </div>-->
  <div class="overflow-auto">


    <b-table
      id="my-table"
      :items="items"
      :per-page="perPage"
      :current-page="currentPage"
      small
    ></b-table>
     <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    >
    </b-pagination>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "ClientsBase",
  data() {
    return {
      perPage: 3,
      currentPage: 1,
      items: [
        {id: 1, name: 'Ольга', mail: '5810@mail.ru'},
        {id: 2, name: 'Ирина', mail: 'ir9128@mail.ru'},
        {id: 3, name: 'Андрей', mail: 'aafedorov@mail.ru'},
        {id: 4, name: 'Константин', mail: 'pavlov123@mail.ru'},
        {id: 5, name: 'Григорий', mail: '47293j@mail.ru'},
        {id: 6, name: 'Ангелина', mail: 'hgjsk2@mail.ru'},
        {id: 7, name: 'Роман', mail: 'mdkm@mail.ru'},
        {id: 8, name: 'Михаил', mail: 'mih120@mail.ru'},
        {id: 9, name: 'Дарья', mail: 'ddria@mail.ru'}
      ]
    }
  },
  computed: {
    rows() {
      return this.items.length
    }
  }

  /*data() {
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
        url: "http://127.0.0.1:8000/clients/",
        methods: 'GET',
        success: (response) => {
          console.log(response);
          this.items = response;

        },
        error: (response) => {
          alert("Невозможно получить базу клиентов ");
          console.log(response)
        }
      })
    }
  }*/
}
</script>

<style scoped>

</style>
