<script>
	import Counter from './Counter.svelte';
	import Chart from './Chart.svelte';

	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<Chart />

	<div class="p-4 w-80 text-white">
		<div class="mb-4 flex justify-between">
			<div class="">Thema:</div>
			<div class="p-2 rounded-md bg-neutral-800">Asyl Politik</div>
		</div>
		<div class="mb-4 flex justify-between">
			<span class="">Partei:</span>
			<span class="p-2 rounded-md bg-blue-700">JUSO</span>
		</div>
		<div class="mb-4 flex justify-between">
			<span class="">Politisches Spektrum:</span>
			<span class="p-2 rounded-md bg-green-700">65% Links</span>
		</div>
		<div class="mb-4 flex justify-between">
			<span class="">Platzhalter</span>
			<span class="p-2 rounded-md bg-neutral-800">Positiv</span>
		</div>
		<div class="mb-4 flex justify-between">
			<span class="">Platzhalter</span>
			<span class="p-2 rounded-md bg-neutral-800">So und so</span>
		</div>
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
