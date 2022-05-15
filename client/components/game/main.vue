<template>
    <box>
      <client-only>
        <swiper
            :effect="'cards'"
            :grabCursor="true"
            :modules="modules"
            :allowSlidePrev="false"
            @slideChange="nextCard"
            @init="createCards"
        >
          <swiper-slide v-for="(slide, index) in slides" :key="index" >
            <GameCard :question="slide.question || ''" 
            :category="slide.category || ''" 
            :player="slide.player || false" 
            :color="slide.color || ''"/>
          </swiper-slide>
        </swiper>
        </client-only>
    </box>
</template>


<script setup>
const props = defineProps({
  categories: {
    type: Array,
    required: true
  },
  players: {
    type: Array,
    required: false
  }
})
const API = useRuntimeConfig().public.baseURL

const slides = ref([{question: 'Daj mi chwilkę...', category: 'Ładowanie'}])
const categories = props.categories.join(",") || 'random'
const players = props.players

const createQuestion = (data) =>{
  const questions = []
    if(data.length > 0){
      data.forEach((question)=>{
        questions.push({
          question: question.question,
          category: question.category
        })
      })
    }
    if(players.length > 1){
      questions.forEach((question)=>{
        const selectedPlayer = players[Math.floor(Math.random() * players.length)]
        question.player = selectedPlayer.name
        question.color = selectedPlayer.color
      })
    }

    slides.value.push(...questions)
}

const createCards = async () => {
  const { items } = await $fetch(`${API}/question?category=${categories}&count=3`)
  slides.value = []
  createQuestion(items)
}
const nextCard = async () =>{
  const { items } = await $fetch(`${API}/question?category=${categories}`)
  createQuestion(items)
}
</script>
<script>
import { Swiper, SwiperSlide } from "swiper/vue"

import "swiper/scss"
import "swiper/scss/effect-cards"

import { EffectCards } from "swiper"

const modules = [EffectCards]

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules
    }
  },
}
</script>

<style lang="scss">
.swiper {
  width: 15rem;
  height: 20rem;
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
.swiper-3d .swiper-slide-shadow{
  display: none;
}
</style>