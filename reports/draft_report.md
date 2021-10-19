# Grid Effects on Turing Patterns in Cellular Automata-Like Models 

Ally Bell and Yehya Albarkri

## Abstract

We are exploring the effects of grid shape on the Turing Patterns that emerge in CA models, particularly based on a model that passes "tokens" between spaces on a hexagonal grid. At this point in our implementation, we've compared the behavior of a square grid to a hexagonal grid in a traditional reaction-diffusion model, without the token implementation used in the Ishida paper. We've observed a distinct difference, and so are moving forward investigating this modification. 

## Annotated Bibliography

Emergence of Turing Patterns in a Simple Cellular Automata-Like Model via Exchange of Integer Values between Adjacent Cells

Ishida, Takeshi, Hindawi Discrete Dynamics in Nature and Society (January 28, 2020)

This paper presents a CA-like model of a simplified Turning pattern model which can produce the characteristic spots and stripes while also being able to support Turing instability. On a hexagonal grid, the model employs a different approach to pattern formation that uses only one type of token. Cells exchange integer values with only adjacent cells, and tokens increase in value as they move. Some token movement is determined by the global algorithm rather than the local, differentiating the model from a typical CA structure. Ishida proposes the application of this model to IOT devices to control data traffic.

## Experiment

Ishida's model overview 

He explains the choice of a hexagonal grid due to the follow reasons:

"(a) In a square grid, the subsequent cell state is based on the states of the considered cell and its eight neighbors. There are only six neighbors in a hexagonal grid, which simplifies the number of transition rules to be considered.

(b) A hexagonal grid is isotropic, whereas a square grid is not. Since this model includes the process of distributing tokens to adjacent cells, it is simpler to apply when the distances between adjacent cells are equal. This model can also be applied to a square grid, but the pattern that is created is not isotropic. Many previous studies, such as those by Adamatzky [26] and Schepers [22] used isotropic grids."

We're exploring this choice - investigating what effects a different grid shape will have on the emerging patterns and how this can influence results. 

In the Ishida Model, there are two possible states a cell can be in (black and white), and each cell can contain tokens that are labeled with integer values and passed between cells. Each time a token moves, it's value increases by one, as seen in the figure below.

![](.\images\hex_grid.PNG)

The black cells act as sources for tokens, with *b* initial tokens on a black cell at each time step. At each time step, the tokens are distributed 

We're implementing our variation on the model using a square grid, where tokens spread to the neighboring eight cells rather than six, as in the hexagonal. 

- Include snippets of our implementation and compare it to the explanation of their experiment.

## Results

For the results, we are expecting a different outcome from the standard reaction-diffusion model. The reason for this is because we are doing two modifcations that are likely to have a significant impact on the model behavior. The first is that we are using a hexagonal grid, rather than a rectangular. The second is that we are using tokens which affect the reaction radius of each cell. As a consequence of this, we will have additional parameters over the standard reaction-diffusion model, but this will also allow us to observe more effects of variable modifications.

One possible manner we can display the results of our two models is through a grid of examples. We can show a row of a variety of tunings for the shared parameters between the models. For the additional parameters, we can provide examples of the new model as columns below the rows. This would create a visually interpretable breakdown of the differences between the models.

We have a diffusion-reaction model implementation of a hexagonal grid and a rectangular grid, and the results alone from these models vary quite a bit. However, we are still in the process of implmenting the token function that is described in the paper. We believe that it will yield even more interesting results.

The following images are of the following parameters: a grid size of 300 x 300, diffusion rate a: 0.5, diffusion rate b: 0.25, feed rate 0.02, kill rate: 0.05, and starting noise with the range of 0 - 0.1. 

![](.\images\normal_rectangular.png)

The image above displays the results using a rectangular grid, where the chemical diffuses equally in all 4 directions.

![](.\images\normal_hex.png)

The image above displays the results using a hexagonal grid, there the chemical diffuses equally in all 6 directions.

As you can see, the results are quite different, and both are interesting in their own way. We look forward to completing Ishida's model to view the results of a different abstraction of reaction-diffusion.

## Conclusions

 We believe that Ishida's model provides a more true-to-life implementation of the standard reaction-diffusion model. The primary effect is that it accounts for various intensities of reactions. This is interpreted as one chemical being able to react with different behavior, according to a different underlying driving factor. An example of this is having a chemical reaction occuring on an unevenly heated surface.

Here we will explain our takes on why the differences are what they are and possible applications of each of these models across various disciplines, even though they were originally modeled after an idea in mind. It is likely that we can observe the pattern from this model in other areas of life as well.
