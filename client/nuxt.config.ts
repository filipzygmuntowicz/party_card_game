import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    css: [
        '@/assets/scss/reset.scss'
    ],
    runtimeConfig: {
        public:{
            baseURL: 'https://justcors.com/tl_265c0cd/https://drinkixxy.herokuapp.com/api/'
        }
    },
    modules: ['./modules/nuxt-icons/module.ts']
})
