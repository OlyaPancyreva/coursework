<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="3000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <b-carousel-slide img-src="https://sun7-6.userapi.com/iDOo0k-gHBQStEcoqYfQTGtMhGTVKifU80LEYg/Yy_v-p41U2w.jpg"></b-carousel-slide>
      <b-carousel-slide img-src="https://sun7-7.userapi.com/On-_LAkKGDxi48W6Z_9ykgd0DjJRX3mMz5wRQA/38MxkeeP9MU.jpg"></b-carousel-slide>
      <b-carousel-slide img-src="https://sun7-9.userapi.com/GzbfxAGFrbo00iInMQqKvYOHD1e8xNSJ9Ria0Q/224j3RYvOVk.jpg"></b-carousel-slide>
      <b-carousel-slide img-src="https://sun9-66.userapi.com/b917XF65FFG42NwpQJ3eL-I9OhSy6m8xHsLD_w/M1gnshZYY3M.jpg"></b-carousel-slide>
      <b-carousel-slide>
<template v-slot:img>
          <img
            class="d-block img-fluid w-100"
            src="../assets/carousel2.png"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

    </b-carousel>
  </div>
</template>

<script>
  export default {
    name: "Carousel",
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>

<style scoped>

</style>
