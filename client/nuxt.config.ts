import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    css: [
        '@/assets/scss/reset.scss'
    ],
    modules: ['./modules/nuxt-icons/module.ts',]
})
