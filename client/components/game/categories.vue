<template>
        <box class="game__box">
            <h1><img src="@/assets/images/logo.svg" alt="Drinking card game"></h1>
            <span class="title">Wybierz kategorie</span>

            <ul class="players">
                <li class="box__input" v-for="category in categories" :key="category">
                    <label>
                        <span class="checkbox__text">{{category.category}} {{category.nsfw ? '(nsfw)' : ''}}</span>
                        <input type="checkbox" :value="category.category" v-model="selectedCategories">
                    </label>
                </li>
            </ul>
            <button type="button" class="submit" @click="$emit('changeStage', { stage: 1, categories: selectedCategories })">Graj</button>
            <button type="button" class="btn-return" @click="$emit('changeStage', {stage: -1})">Wróć</button>
        </box>
</template>

<script setup>

const { items: categories } = await $fetch('https://justcors.com/tl_3adbbae/https://drinkixxy.herokuapp.com/api/categories')

const selectedCategories = ref([])

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
    align-items: center;
    label{
        display: flex;
        width: 100%;
        gap: 1rem;
        justify-content: center;
        align-items: center;
    }
    input{
        padding: 0.5em 1em;
        font-size: 1em;
        font-family: "Poppins", sans-serif;
        border-radius: 50em;
        border: none;
        width: 80%;
    }
    input[type="checkbox"]{
        width: 2.2rem;
        height: 2.2rem;
        border-radius: 100%;
    }
    .checkbox__text{
        padding: 0.5em 1em;
        font-size: 1em;
        font-family: "Poppins", sans-serif;
        border-radius: 50em;
        border: none;
        width: 80%;
        background-color: #fff;
        text-align: left;
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