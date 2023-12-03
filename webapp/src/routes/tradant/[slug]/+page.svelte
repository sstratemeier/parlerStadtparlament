
<script>
import tradants from '../../tradants';
import { page } from '$app/stores';

let tradant = {
    name: "",
}; 

console.log($page.params.slug);
tradant = tradants[$page.params.slug] || {};

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
				{ tradant.name }
			</div>
			<div class="article-abstract italic mb-4">
				In einer detaillierten Anfrage an das Stadtparlament St. Gallen hinterfragt Andrea Scheck,
				Stadtparlamentarierin der JUSO, die Haftbedingungen im Ausschaffungsgefängnis Bazenheid und
				die Praxis der Überstellung abgewiesener Asylsuchender aus St. Gallen in diese Einrichtung.
			</div>
			<div class="article-text mb-8">
				Der Text beinhaltet eine Anfrage an das Stadtparlament St. Gallen bezüglich der
				Haftbedingungen im Ausschaffungsgefängnis Bazenheid und der Überstellung abgewiesener
				Asylsuchender dorthin. Die Anfrage thematisiert die Einhaltung von Mindeststandards,
				mangelnde Alternativen zu diesen Gefängnissen und die Prüfung der Rechtmäßigkeit und
				Angemessenheit der Haft. Der Stadtrat erkennt an, dass nur Mindestanforderungen erfüllt
				werden, sieht jedoch keine unmittelbaren Alternativen, bis die geplante Erweiterung des
				Regionalgefängnisses Altstätten realisiert ist.
			</div>
			<div class="article-navigation-bar flex justify-between text-white text-s mb-4">
				<div class="previous-session p-4 rounded-md bg-neutral-600">
					<div>
						<div>Sitzung davor</div>
						<div class="text-gray-400 font-bold">22.12.2023</div>
					</div>
				</div>

				<div class="next-session p-4 rounded-md bg-neutral-600 text-right">
					<div>
						<div>Sitzung danach</div>
						<div class="text-gray-400 font-bold">23.12.2023</div>
					</div>
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
