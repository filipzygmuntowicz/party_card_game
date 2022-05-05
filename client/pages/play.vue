<template>
    <section class="game">
        <GamePlayers v-if="stage === 1" @changeStage="changeStage"/>
        <GameCategories v-if="stage === 2" @changeStage="changeStage"/>
        <GameMain v-if="stage === 3" />
    </section>
</template>
<script setup>
const stage = ref(1)
const changeStage = (value)=>{
    if(value.stage > 0){
        stage.value = stage.value + +value.stage
    }else{
        stage.value = stage.value - Math.abs(value.stage)
    }
}
</script>
<style lang="scss" scoped>
.game{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 50 50'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%239C92AC' transform='matrix(0.875, 0.485, -0.485, 0.875, 8.042, -4.079)' fill-opacity='0.08'%3E%3Cpath d='M20.832,4.555A1,1,0,0,0,20,3H4a1,1,0,0,0-.832,1.554L11,16.3V20H8v2h8V20H13V16.3L20.832,4.555ZM18.132,5l-2,3H7.868l-2-3Z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
</style>