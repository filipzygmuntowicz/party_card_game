<template>
        <box class="game__box">
            <h1><img src="@/assets/images/logo.svg" alt="Drinking card game"></h1>
            <span class="title">Dodaj graczy</span>
            <div class="box__input">
                <input type="text" placeholder="John Doe" v-on:keyup.enter="addPlayer"/>
                <button type="button" class="btn btn-success" @click="addPlayer"><nuxt-icon name="plus" /></button>
            </div>
            <template v-if="players.length">
                <span class="title">Gracze</span>
                <ul class="players">
                    <li class="box__input" v-for="player in players" :key="player">
                        <input type="text" readonly :value="player.name" :data-id="player.id">
                        <button type="button" class="btn btn-danger" @click="removePlayer"><nuxt-icon name="minus" /></button>
                    </li>
                </ul>
                <button type="button" class="submit" @click="$emit('changeStage', { stage: 1, players: players })">Graj</button>
            </template>
            <template v-else>
                <p class="additionaltext"> Wolisz grać po swojemu? </p>
                <button type="button" class="submit" @click="$emit('changeStage', { stage: 1 })">Graj bez graczy</button>
            </template>
            <NuxtLink  class="btn-return" to="/#hero">Wróć</NuxtLink>
        </box>
</template>

<script setup>
const players = ref([])
const addPlayer = (ev) => {
    const input = getInput(ev)
    if(input.value.trim() !== ""){
        players.value.push({
            id: players.value.length,
            name: input.value
        })
        input.value = ""
    }else{
        console.log("PUSTO") // TODO: Obsłużyć błędy
    }
}
const removePlayer = (ev) => {
    const input = getInput(ev)
    console.log(input)
    const id = input.dataset.id 
    players.value = players.value.filter((player)=> player.id !== +id)
}
const getInput = (ev) => {
    if(ev.target.tagName.toLowerCase() === 'input'){
        return ev.target
    }
    return ev.target.closest('button').closest('.box__input').querySelector('input')
}
</script>

<style lang="scss" scoped>
.additionaltext{
    color: #eee;
    margin-top: 2em;
}
.game__box{
    display: flex;
    flex-direction: column;
}
h1{
    margin-bottom: 2rem;
    img{
        width: 24em;
    }
}
.title{
    color: #fff;
    margin-bottom: 1rem;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 1em;
    margin-top: 1rem;
    &:first-of-type{
        margin-top: 0;
    }
}
.box__input{
    display: flex;
    gap: 1rem;
    justify-content: center;
    input{
        padding: 0.5em 1em;
        font-size: 1em;
        font-family: "Poppins", sans-serif;
        border-radius: 50em;
        border: none;
        width: 80%;
    }
    .btn{
        width: 2.2rem;
        height: 2.2rem;
        border-radius: 100%;
        border: none;
        font-size: 1em;
        color: #fff;
        cursor: pointer;
        transition: background-color 0.3s;
        &.btn-success{
            background-color: #61d39a;
            &:hover{
                background-color: #138056;
            }
        }
        &.btn-danger{
            background-color: #d37461;
            &:hover{
                background-color: #801313;
            }
        }
        &:hover{
            transition: background-color 0.3s;
        }
    }
}
.players{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.5em;
    align-items: center;
    li{
        width: 100%;
    }
}
.submit{
    display: inline-block;
    margin-top: 2rem;
    padding: 1rem 7rem;
    background: linear-gradient(#188D53, #25DE38);
    font-family: "Raleway", sans-serif;
    text-transform: uppercase;
    text-decoration: none;
    color: #FFF;
    font-weight: 900;
    letter-spacing: 1px;
    border-radius: 15px;
    position: relative;
    z-index: 1;
    font-size: 1.2em;
    transition: transform 0.2s;
    border: none;
    cursor: pointer;
    &::after{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        backdrop-filter: blur( 15px );
        border-radius: 15px;
        z-index: -1;
    }
    &:hover{
        transform: scale(0.95);
        transition: transform 0.2s;
        &::after{
            opacity: 0;
        }
    }
}
</style>