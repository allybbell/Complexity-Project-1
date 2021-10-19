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

## Results

v different

## Conclusions

 

