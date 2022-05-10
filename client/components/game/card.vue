<template>
    <article class="card" v-if="!empty">
        <div class="card__top">{{props.category}}</div>
        <div class="card__content" :class="{ 'only': !props.player }">{{props.question}}</div>
        <div class="card__bottom" v-if="props.player" :style="props.color ? `background-color: ${props.color}` : ''">
            <span class="card__player"> <nuxt-icon name="user"/> {{props.player}}</span>
        </div>
    </article>
    <article v-else class="card--empty">
    </article>
</template>

<script setup>
const props = defineProps({
  question: {
    type: String,
    required: false
  },
  player: {
      type: [String, Boolean],
      default: false
  },
  category: {
      type: String,
      default: 'Sport'
  },
  color: {
      type: String
  }
})

const empty = ref(true)
if(props.question || props.first){
    empty.value = false
}
if(process.client){
    if(props?.color && props?.color === "random"){
        const randomColor = Math.floor(Math.random() * (360 - 0 + 1))
        document.querySelector('.card__bottom').style.backgroundColor = `hsla(${randomColor}deg, 100%, 70%, 1)`
    }
}

</script>

<style lang="scss" scoped>
.card{
    width: 15rem;
    height: 20rem;
    background-color: #FFFFFF;
    border-radius: 15px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
    box-shadow: 8px 8px 24px 0px rgba(66, 68, 90, 1);
}
.card.first{
    background-color: #761774;
    justify-content: center;
    gap: 2em;
    box-shadow:
    0 0 50px -20px rgb(255, 21, 130)
}
.card.first{
    background-color: #761774;
    justify-content: center;
    gap: 2em;
    box-shadow:
    0 0 50px -20px rgb(255, 21, 130)
}

.card--empty{
    width: 15rem;
    height: 20rem;
    // background-color: #FFFFFF;
    border-radius: 15px;
    backdrop-filter: blur( 2px );
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
}
.card__top{
    line-height: 150%;
    width: 100%;
    background-color: #FDE090;
    display: block;
    height: 20%;
    text-align: center;
    font-weight: 900;
    font-family: "Raleway", sans-serif;
    text-transform: uppercase;
    color: #2B2B2B;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-bottom: 0.5rem;
    &::after{
        content: "";
        position: absolute;
        left: 0;
        bottom: -0.5rem;
        background-color: #fff;
        width: 100%;
        height: 1rem;
        border-radius: 50%;
    }
}
.card__content{
    font-weight: 900;
    font-family: "Raleway", sans-serif;
    padding: 0 1em;
    line-height: 120%;
    letter-spacing: 0.5px;
    color: #222;
    font-size: 0.7em;
}
.card__content.only{
    flex-grow: 0.5;
}
.card__bottom{
    width: 100%;
    height: 25%;
    background-color: #7595ff;
    text-align: center;
    font-weight: 900;
    font-family: "Raleway", sans-serif;
    text-transform: uppercase;
    color: #ffffff;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 0.5rem;
    &::after{
        content: "";
        position: absolute;
        left: 0;
        top: -0.5rem;
        background-color: #fff;
        width: 100%;
        height: 1rem;
        border-radius: 50%;
    }
}
.card__player{
    padding: 0.6rem 2rem;
    background-color: rgba(0,0,0,0.4);
    border-radius: 25rem;
    font-size: 0.65em;
}
</style>