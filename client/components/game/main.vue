<template>
    <box>
        <swiper
            :effect="'cards'"
            :grabCursor="true"
            :modules="modules"
            class="mySwiper"
        >
        <swiper-slide><GameCard question="Dlaczego jesteś taki?" /></swiper-slide>
        <swiper-slide><GameCard question="Dlaczego jesteś taki?2" /></swiper-slide>
        <swiper-slide><GameCard question="Dlaczego jesteś taki?3" /></swiper-slide>
        </swiper>
    </box>
</template>

<script>
import { Swiper, SwiperSlide } from "swiper/vue"

import "swiper/css"
import "swiper/css/effect-cards"

import { EffectCards } from "swiper"

const modules = [EffectCards]

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules,
    };
  },
};


</script>
<script setup>

</script>

<style lang="scss">

.swiper {
  width: 240px;
  height: 320px;
}

.swiper-slide {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 18px;
  font-size: 22px;
  font-weight: bold;
  color: #fff;
}
</style>