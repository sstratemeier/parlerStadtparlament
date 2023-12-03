<script>
	import Counter from './Counter.svelte';
	import Chart from './Chart.svelte';

	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';

	import tradants from './tradants';

	import Icon from '@iconify/svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<div class="flex space-x-16">
		<div class="infocard p-4 w-80 text-white">
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

		<div class="article-wrapper text-yellow-100 max-w-xl">
			<div class="article-info-bar flex text-s mb-4">
				<div class="article-date mr-8">Samstag, 23.12.2023</div>
				<div class="article-info-title">Stadtparlaments Sitzung</div>
			</div>
			<div class="article-header text-xl font-bold mb-4">
				Untersuchung der Haftbedingungen und Überstellungspraktiken im Ausschaffungsgefängnis
				Bazenheid
			</div>
			<div class="article-abstract italic mb-4">
				In einer detaillierten Anfrage an das Stadtparlament St. Gallen hinterfragt Andrea Scheck,
				Stadtparlamentarierin der JUSO, die Haftbedingungen im Ausschaffungsgefängnis Bazenheid und
				die Praxis der Überstellung abgewiesener Asylsuchender aus St. Gallen in diese Einrichtung.
			</div>
			<div class="article-text mb-16">
				Der Text beinhaltet eine Anfrage an das Stadtparlament St. Gallen bezüglich der
				Haftbedingungen im Ausschaffungsgefängnis Bazenheid und der Überstellung abgewiesener
				Asylsuchender dorthin. Die Anfrage thematisiert die Einhaltung von Mindeststandards,
				mangelnde Alternativen zu diesen Gefängnissen und die Prüfung der Rechtmäßigkeit und
				Angemessenheit der Haft. Der Stadtrat erkennt an, dass nur Mindestanforderungen erfüllt
				werden, sieht jedoch keine unmittelbaren Alternativen, bis die geplante Erweiterung des
				Regionalgefängnisses Altstätten realisiert ist.
			</div>
			<div class="article-navigation-bar flex justify-between text-white text-right text-s mb-4 ">
				<div class="previous-session p-4 rounded-md bg-neutral-600 flex gap-x-3 items-center">
					<Icon class="w-8 h-8" icon="material-symbols:arrow-left-alt" />
					<div>
						<div>Sitzung davor</div>
						<div class="text-gray-400 font-bold">22.12.2023</div>
					</div>
				</div>

				<div class="next-session p-4 rounded-md bg-neutral-600 text-left flex gap-x-3 items-center">
					<div>
						<div>Sitzung danach</div>
						<div class="text-gray-400 font-bold">23.12.2023</div>
					</div>
					<Icon class="w-8 h-8" icon="material-symbols:arrow-right-alt" />
				</div>
			</div>
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
