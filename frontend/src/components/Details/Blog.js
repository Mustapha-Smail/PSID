import React from 'react'
import { Link } from 'react-router-dom'
import './Blog.css'
const Blog = () => {
    return (
        <>
            <div className='title'>
                <h1>Rapport & Synthèse</h1>
            </div>
            <main>
                <section>
                    <h2>Introduction</h2>

                    <div>Afin de pouvoir réaliser notre dashboard, nous sommes passés au travers de plusieurs étapes.</div>
                    <ol>
                        <li>Charger les données :</li>
                        <p>
                            <span>Nous avons commencé par importer les données depuis un fichier CSV se trouvant sur </span>
                            <span><a href="https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants">Kaggle</a></span>
                            <span> concernant les fiches de notations TripAdvisor de restaurants de la plupart des pays européens (hors Russie).</span>
                        </p>
                        <li>Nettoyer les données : </li>
                        <p>Après avoir chargé les données, nous avons effectué quelques étapes pour les nettoyer. Cela implique généralement de supprimer ou de corriger les données qui sont incomplètes ou mal formatées. Dans notre cas, nous avons enlevé les lignes de données qui manquaient d'informations essentielles dans certaines colonnes, comme le nom du restaurant, le pays, le niveau de prix, etc. Nous sommes donc passés de 1 083 397 lignes initialement à 190 325 lignes.</p>
                        <li>Simplifier les données : </li>
                        <p>Nous avons également simplifié certaines informations. Par exemple, pour la colonne 'cuisines' qui pouvait contenir plusieurs types de cuisine par restaurant, nous avons décidé de ne garder que le premier type de cuisine que l’on a considéré comme étant le type de cuisine principale (Bar, Italienne, Méditerranéenne,...).</p>

                    </ol>
                </section>
                <section>
                    <h2>Les connaissances surprenantes que nous avons tirés de l’analyse de ce tableau de bord</h2>
                    <div>
                        <details>
                            <summary>
                                Les pays ayant le plus de restaurants proposant des adaptations diététiques ne sont pas forcément ceux dont la part est la plus élevée.
                            </summary>
                            <span>La carte </span>
                            <span>
                                <Link to={'/dashboard#distribution-restaurants'}>
                                    "Distribution des restaurants spécifiques au régimes"
                                </Link>
                            </span>
                            <span> nous montre que contrairement à ce que nous avait fait penser le diagramme </span>
                            <span>
                                <Link to={'/dashboard#price-diet'}>
                                    "Adaptations diététiques dans les restaurants par pays"
                                </Link>
                            </span>
                            <span>, les pays ayant le plus de restaurants proposant des adaptations diététiques ne sont pas forcément ceux dont la part est la plus élevée. Par exemple, la France est l’un des pays ayant le plus d’adaptation diététique mais sa part en prenant le nombre total de restaurants est l’une des plus faibles d’europe </span><br />
                            On remarque aussi que certains pays qui n’ont pas énormément de restaurants proposent tout de même plus d’adaptation en moyenne ce qui montre que le régime alimentaire entre en compte dans les adaptations des restaurants.
                        </details>
                    </div>
                    <div>
                        <details>
                            <summary>
                                La tendance concernant l’évolution du régime alimentaire des européens.
                            </summary>
                            Un des points surprenant que nous avons remarqué en travaillant sur ce dataset est la tendance concernant l’évolution du régime alimentaire des européens. En effet, ces dernières années, on pouvait constater que la tendance vers un régime alimentaire végan ou végétarien prenait de l’ampleur. De nos jours, ce changement marque un tournant significatif dans les habitudes alimentaires des européens, on peut notamment le voir dans le graphique présentant les Adaptations Diététiques dans les restaurants des pays de européens. <br />
                            Cette visualisation nous permet de faire un constat sur l’adaptation qu'ont les restaurateurs dans leur démarche de proposer des menus végan ou végétarien. Toutes ces adaptations et changements seraient potentiellement dûes à une conscience environnementale de plus en plus présente, une prise de conscience en termes de surconsommation de viande entraînant des problèmes de santé ou la question sur le bien-être animal.
                        </details>
                    </div>
                    <div>
                        <details>
                            <summary>
                                Il semble y avoir un lien entre la note générale d’un restaurant, et la note évaluant son rapport qualité-prix d’un restaurant.  <br />
                            </summary>
                            Ce qui semble logique de prime abord, cependant le fait que ce lien soit aussi fort ne l'est pas tout autant. En effet, la note moyenne et le rapport qualité-prix (RQP) moyen sont très proches en termes de valeurs. Celles-ci étant situées autour de (4/5)
                        </details>
                    </div>
                    <div>
                        <details>
                            <summary>
                                Une observation intéressante que l’on a pu faire concerne le rapport qualité-prix.   <br />
                            </summary>
                            En effet, on aurait pu penser qu’il existe des disparités énormes concernant la perception des clients ayant donné leur avis sur le sujet. Pourtant, on se rend compte que le niveau de satisfaction ne semble pas diminuer fortement avec l’augmentation du prix. Preuve en est, les niveaux de satisfaction pour les niveaux de prix moyen (€€-€€€) et les plus élevés (€€€€) se confondent. De plus, le niveau de satisfaction médian est équivalent (4,5/5) pour l’ensemble des niveaux étudiés.
                        </details><br /><br /><br />
                    </div>
                </section>
                <section>
                    <h2>Machine Learning</h2>
                    <h3>K-Means</h3><br />
                    <div>K-Means est un algorithme d'apprentissage non supervisé utilisé pour regrouper des données en groupes distincts en fonction de leur similarité. Il partitionne un ensemble de données en K clusters, où chaque point de données appartient au cluster avec la moyenne ou le centroïde le plus proche. Il est largement utilisé dans divers domaines tels que l'apprentissage automatique, l'extraction de données et la reconnaissance de motifs.</div><br />

                    <h3>Nombre de clusters et évaluation de qualité</h3>
                    <h4>Nombre de clusters</h4><br />
                    <div>Pour déterminer le nombre optimal de clusters dans le contexte de l'application de K-Means à la segmentation des restaurants, nous avons utilisé la méthode du coude. La méthode du coude consiste à exécuter l'algorithme K-Means pour différents nombres de clusters (de 1 à un nombre maximum raisonnable) et à observer comment l'inertie intra-cluster (la somme des carrés des distances des points de données à leur centroïde respectif) évolue en fonction du nombre de clusters. Ensuite, on cherche le point où l'inertie commence à diminuer de manière marginale, formant ainsi une courbe qui ressemble à un "coude". Ce point indique généralement le nombre optimal de clusters à choisir. Dans notre cas, après avoir appliqué cette méthode, nous avons déterminé que choisir entre 13 et 17 clusters étaient appropriés pour regrouper les restaurants en fonction de leurs caractéristiques telles que le niveau de prix, les offres végétariennes, les options végétaliennes, les offres sans gluten et les notes moyennes. Ces clusters seront ensuite utilisés pour recommander des restaurants similaires aux utilisateurs en fonction de leurs préférences.</div><br />
                    <h4>Qualité des clusters</h4><br />
                    <div>Pour déterminer le nombre optimal de clusters dans le contexte de l'application de K-Means à la segmentation des restaurants, nous avons également utilisé le Silhouette Score. Le Silhouette Score est une métrique qui évalue la qualité des clusters formés par K-Means en mesurant à quel point les objets d'un cluster sont similaires les uns aux autres par rapport aux objets des autres clusters. Un score Silhouette proche de 1 indique que les clusters sont bien séparés et que les points de données sont proches de leur propre cluster et éloignés des autres clusters.</div>
                    <div>Dans notre cas, après avoir appliqué le Silhouette Score pour différents nombres de clusters, nous avons obtenu un score de 0,6446 pour 15 clusters. Cela signifie que les restaurants regroupés dans ces 15 clusters sont relativement bien séparés les uns des autres, ce qui est un indicateur positif de la qualité de la segmentation. Ainsi, en utilisant 15 clusters, nous pouvons recommander des restaurants aux utilisateurs en fonction de leurs préférences, en nous assurant que les restaurants dans chaque cluster sont similaires en termes de caractéristiques telles que le niveau de prix, les offres végétariennes, les options végétaliennes, les offres sans gluten et les notes moyennes. Ce score Silhouette de 0,6446 renforce la confiance dans la pertinence de notre choix de nombre de clusters pour cette application spécifique.</div><br />

                    <h3>Selection des critères</h3><br />
                    <div>Dans ce contexte, K-Means est utilisé pour identifier les structures liées aux données des restaurants afin de pouvoir proposer à l’utilisateur une liste de restaurants se rapprochant le plus de ses critères. Ici,les critères possibles comprennent des caractéristiques telles que le niveau de prix, les offres végétarienne, les options végétaliennes, les offres sans gluten et les notes moyennes. En appliquant K-Means, nous cherchons à regrouper des restaurants similaires en fonction de ces caractéristiques.</div>
                    <div>Certaines variables n’étant pas utilisables en l’état par l’algorithme K-Means, nous avons dû les encoder. Ainsi les variables booléennes telles que les offres végétariennes, les options végétaliennes et les offres sans gluten ont été encodées avec un encodage binaire et les niveaux de prix avec un encodage de label, permettant leur conversion en format numérique.</div>
                    <div>Comme dit précédemment, nous avons décidé de garder uniquement les variables nécessaires à l'application de K-means ainsi que les identifiants de nos restaurants (restaurant_link).</div>
                </section>
            </main>
        </>
    )
}

export default Blog