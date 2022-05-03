<template>
    <MainHero />
</template>

<style lang="scss">
body {
	background: linear-gradient(-45deg, #ee7752, #e73c7e, #5E0C46, #0B163A);
	background-size: 400% 400%;
	animation: gradient 20s ease infinite;
	height: 100vh;
}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}

</style>