<template>
    <div id="app">
      <Header></Header>
      <router-view/>
    </div>
</template>
<style>
  #app {
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    margin-left: auto;
    margin-right: auto;
    background: url("https://sun7-7.userapi.com/gSWApQS-G9a-jCacdi84o1DySWBQvT8wr_KpPA/WqhZ3UDWk70.jpg") fixed no-repeat;
    background-size: 100%;
  }
  .btn-wid {
    padding: 20px;
    margin: 20px;
    width: 400px;
  }

  .buts {
    margin-top: 100px;
    margin-left: 200px;
    margin-right: 200px;
  }

  .my-card {
    background: url("https://sun7-7.userapi.com/gSWApQS-G9a-jCacdi84o1DySWBQvT8wr_KpPA/WqhZ3UDWk70.jpg") fixed no-repeat;
    background-size: 100%;
  }

  .my-card2 {
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 100px;
  }

  .btn-r{
    float: right;
    margin: 20px;
  }

</style>
<script>
  import Header from "./components/Header";
  import Footer from "./components/Footer";

  export default {
    name: 'App',
    components: {
      Footer,
      Header,
    },
  };
</script>
