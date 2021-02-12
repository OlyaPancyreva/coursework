<template>
  <b-card class="my-card">
    <b-aspect :aspect="2">
      <b-card class="buts">
        <b-aspect :aspect="16">
          <div>
            <b-navbar type="light" variant="light" id="nav">
              <b-navbar-nav>
                <b-nav-item-dropdown text="Заявки" right style="margin-left: 20px">
                  <b-dropdown-item href="#" v-on:click="requestTourClick">Забронированные туры</b-dropdown-item>
                  <b-dropdown-item href="#" v-on:click="requestClick">Заявки на обратный звонок</b-dropdown-item>
                </b-nav-item-dropdown>

                <b-nav-item-dropdown text="Туры" right style="margin-left: 20px">
                  <b-dropdown-item href="#" v-on:click="newTourClick">Добавить новый тур</b-dropdown-item>
                </b-nav-item-dropdown>

                <b-nav-item-dropdown text="База" right style="margin-left: 20px">
                  <b-dropdown-item href="#" v-on:click="requestClientClick">База клиентов</b-dropdown-item>
                  <b-dropdown-item href="#" v-on:click="requestSoldTour">База проданных туров</b-dropdown-item>
                </b-nav-item-dropdown>
              </b-navbar-nav>
            </b-navbar>
          </div>
          <RequestList v-show="request"></RequestList>
          <NewTour v-show="newTour"></NewTour>
          <AllBookedTour v-show="requestTour"></AllBookedTour>
          <ClientsBase v-show="clientBase"></ClientsBase>
          <SoldTour v-show="soldTour"></SoldTour>
        </b-aspect>
      </b-card>
    </b-aspect>
  </b-card>
</template>
<script>
  import Header from "./Header";
  import AllTour from "./AllTour";
  import HotTour from "./HotTour";
  import RequestList from "./RequestList";
  import NewTour from "./NewTour";
  import $ from "jquery";
  import AllBookedTour from "./AllBookedTour";
  import ClientsBase from "./ClientsBase";
  import SoldTour from "./SoldTour";

  export default {
    name: "AdminPage",
    components: {SoldTour, ClientsBase, AllBookedTour, NewTour, RequestList, Header, AllTour, HotTour},
    data() {
      return {
        request: false,
        newTour: false,
        requestTour: false,
        clientBase: false,
        soldTour: false,
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
    },
    methods: {
      clean() {
        this.request = false;
        this.newTour = false;
        this.requestTour = false;
        this.clientBase = false;
        this.soldTour = false;
      },
      requestClick() {
        this.clean();
        this.request = true;
      },
      newTourClick() {
        this.clean();
        this.newTour = true;
      },
      requestTourClick(){
        this.clean();
        this.requestTour = true;
      },
      requestClientClick(){
        this.clean();
        this.clientBase = true;
      },
      requestSoldTour(){
        this.clean();
        this.soldTour = true;
      }
    }
  }
</script>

<style scoped>
  template {
    background-color: #0d47a1;
  }


</style>
