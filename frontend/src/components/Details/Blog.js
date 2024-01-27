import React from 'react'
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
                            <span> concernant les fiches de notations TripAdvisor de restaurants de la plupart des pays européens (hors Russie libérer l'Ukraine).</span>
                        </p>
                        <li>Nettoyer les données : </li>
                        <p>Après avoir chargé les données, nous avons effectué quelques étapes pour les nettoyer. Cela implique généralement de supprimer ou de corriger les données qui sont incomplètes ou mal formatées. Dans notre cas, nous avons enlevé les lignes de données qui manquaient d'informations essentielles dans certaines colonnes, comme le nom du restaurant, le pays, le niveau de prix, etc. Nous sommes donc passés de 1 083 397 lignes initialement à 190 325 lignes.</p>
                        <li>Simplifier les données : </li>
                        <p>Nous avons également simplifié certaines informations. Par exemple, pour la colonne 'cuisines' qui pouvait contenir plusieurs types de cuisine par restaurant, nous avons décidé de ne garder que le premier type de cuisine que l’on a considéré comme étant le type de cuisine principale (Bar, Italienne, Méditerranéenne).</p>

                    </ol>
                </section>
                <section>
                    <h2>Les connaissances surprenantes que nous avons tirés de l’analyse de ce tableau de bord</h2>
                    <div>
                        <details>
                            <summary>
                                Les pays ayant le plus de restaurants proposant des adaptations diététiques ne sont pas forcément ceux dont la part est la plus élevée.
                            </summary>
                            La carte nous montre que contrairement à ce que nous avait laissé penser le diagramme en bar, les pays ayant le plus de restaurants proposant des adaptations diététiques ne sont pas forcément ceux dont la part est la plus élevée. Par exemple la France est l’un des pays ayant le plus d’adaptation diététique mais sa part en prenant le nombre total de restaurants est l’une des plus faibles d’europe <br />
                            On remarque aussi que certains pays qui n’ont pas énormément de restaurants proposent tout de même plus d’adaptation en moyenne ce qui montre que le régime alimentaire entre en compte dans les adaptations des restaurants.
                        </details>
                    </div>
                    <div>
                        <details>
                            <summary>
                                La tendance concernant l’évolution du régime alimentaire des européens.
                            </summary>
                            Un des points marquants qu’on a remarqué en travaillant sur ce dataset est la tendance concernant l’évolution du régime alimentaire des européens. En effet, ces dernières années, on pouvait constater que la tendance vers un régime alimentaire végan ou végétarien prenait de l’ampleur. De nos jours, ce changement marque un tournant significatif dans les habitudes alimentaires des européens, on peut notamment le voir dans le graphique présentant les Adaptations Diététiques dans les restaurants dans les pays de l’Europe. <br />
                            Cette visualisation nous permet de faire un constat sur l’adaptation qu'ont les restaurateurs dans leur démarche de proposer des menus végan ou végétarien. Toutes ces adaptations et changements seraient potentiellement dûes à une conscience environnementale de plus en plus présente, une prise de conscience en termes de surconsommation de viande entraînant des problèmes de santé ou la question sur le bien-être animal.

                        </details>
                    </div>
                    <div>
                        <details>
                            <summary>
                                Il semble y avoir un lien entre la note générale d’un restaurant, et la note évaluant son rapport qualité-prix d’un restaurant.  <br />
                            </summary>
                            Ce qui semble logique de prime abord, cependant ce qui est surprenant et le fait que ce lien semble aussi fort. En effet, la note moyenne et le rapport qualité-prix (RQP) moyen sont très proches en termes de valeurs. Celles-ci étant situées autour de (4/5)
                        </details>
                    </div>
                    <div>
                        <details>
                            <summary>
                                Une observation intéressante que l’on a pu faire concerne le rapport qualité-prix.   <br />
                            </summary>
                            En effet, on aurait pu penser qu’il existe des disparités énormes concernant la perception des clients ayant donné leur avis sur le sujet. Pourtant, on se rend compte que le niveau de satisfaction ne semble pas diminuer fortement avec l’augmentation du prix. Preuve en est, les niveaux de satisfaction pour les niveaux de prix moyen (€€-€€€) et les plus élevés (€€€€) se confondent. De plus, le niveau de satisfaction médian est équivalent (4,5/5) pour l’ensemble des niveaux étudiés. Ce qui par rapport aux interprétations que nous ont apportés les analyses précédentes nous inforle
                        </details>
                    </div>
                </section>
            </main>
        </>
    )
}

export default Blog