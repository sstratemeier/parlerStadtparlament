
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
			<div class="mb-4 flex justify-between items-center">
				<div class="">Thema:</div>
				<div class="p-2 rounded-md bg-neutral-800">Finanzverwaltung</div>
			</div>
			<div class="mb-4 flex justify-between items-center">
				<span class="">Partei:</span>
				<span class="p-2 rounded-md bg-blue-700">JUSO</span>
			</div>
			<div class="mb-4 flex justify-between items-center">
				<span class="">Politisches Einordnung:</span>
				<span class="p-2 rounded-md bg-green-700">40% Rechts</span>
			</div>
			<div class="mb-4 flex justify-between items-center">
				<span class="">Finanzieller Effekt</span>
				<span class="p-2 rounded-md bg-neutral-800">Einsparung</span>
			</div>
			<div class="mb-4 flex justify-between items-center">
				<span class="">Zeithorizont</span>
				<span class="p-2 rounded-md bg-neutral-800">Langfristig</span>
			</div>
		</div>

		<div class="article-wrapper text-zinc-100 max-w-xl">
			<div class="article-info-bar flex text-s mb-4">
				<div class="article-date mr-8">Samstag, 23.12.2023</div>
				<div class="article-info-title">Stadtparlaments Sitzung</div>
			</div>
			<div class="article-header text-xl font-bold mb-4">
				Analyse der Staatsbeiträge und Finanzkontrolle in St. Gallen
			</div>
			<div class="article-abstract italic mb-4">
				In dieser Analyse wird die Anfrage von René Neuweiler bezüglich der Verwendung von „à fonds perdu“-Staatsbeiträgen in St. Gallen und die darauf folgende Antwort des Stadtrats untersucht.
			</div>
			<div class="article-text mb-8">
				René Neuweiler, Stadtparlamentarier, stellte eine Anfrage über die Praxis der „à fonds perdu“-Staatsbeiträge in St. Gallen. Der Stadtrat erklärte, dass solche Beiträge, die nicht rückzahlbar sind, selten gewährt werden. Die meisten Beiträge sind für spezifische Zwecke und mit Auflagen verbunden, wie z.B. Investitionen in Alters- und Pflegeheime oder Sportinfrastruktur. Größere Beiträge sind an Leistungsvereinbarungen geknüpft, wie die Unterstützung großer Kultureinrichtungen. Einige kleine Beiträge fallen unter „à fonds perdu“, werden jedoch aufgrund geringer Beträge ohne weiteres Controlling ausgezahlt. Der Stadtrat betont, dass ein umfassendes Controlling unpraktikabel und aufgrund der Effizienz nicht umsetzbar wäre.
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
