<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Vijaya Sindhu Dandeboina (vd345)</td></tr>
<tr><td> <em>Generated: </em> 4/23/2023 5:58:39 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vd345" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233820236-d8121b24-c54e-4163-b462-562c80dd1077.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>add item page with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233820300-6cad039d-1928-4311-9717-d45c4824aeda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the products table from DB with filled data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <div>After entering the values in the add page, the values go to the<br>item function in shop.py.&nbsp;</div><div>It checks whether an id is passed to check if<br>the action is to edit or add. As no id will be</div><div>passed this<br>is a create action and a INSERT statement is executed passing</div><div>the values to<br>Products table and is success a flash is displayed.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vd345-prod.herokuapp.com/">https://is601-vd345-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233820458-dddabf42-cc36-4de8-a5e4-21dfed6b3457.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233862785-275bddce-cff4-4960-94c3-6dc380c2d2da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233862846-0430d266-bb5c-44df-aaf9-3886530f1bbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233863034-339ff290-9c40-421f-8856-56a9269c8158.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233863143-5698c73a-6d8c-426f-b10b-796fe08b5d32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop results with category &quot;Food&quot; filter and price: High to Low sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233863564-d4b5d0cc-48f9-4bd5-b4bf-d4055580c394.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing filter/sort logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div>For the shop page,&nbsp; initially we get the items &amp; details from Products</div><div>table<br>whose visibility is 1. and in the page we can search by name</div><div>or<br>select a category or sort on price "High to Low" or "Low</div><div>to High".<br>When we search using one/all of the above option. we go to shop_list<br>function in shop.py and based on the input we add a where</div><div>&nbsp;condition to<br>the query. and display the results again.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vd345-prod.herokuapp.com/">https://is601-vd345-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233864269-1c17a6d7-68f5-416b-8cde-549d89909c19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin view of products list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div>We select all fields from Products table without any filter and pass it</div><div>to<br>the html page.</div><div>As no where condition is specified, every product will be</div><div>displayed irrespective<br>of visibility status</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vd345-prod.herokuapp.com/">https://is601-vd345-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233865683-167c018b-a514-404f-b5ee-8722bfbd9d67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button for admin on shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233865608-482df093-4254-4fcf-b9c1-62a4cfa1c2b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button in item details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233865726-5d57a2d0-366d-4075-a1be-0763ebe8eda4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin list page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233865931-58650fb0-0417-4506-bf14-fece8fde4d27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit page before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233865965-b347dbcf-4bc5-43f8-a9da-fada6e65186e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated the name shirt to shirt for me<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>For the Shop page,&nbsp;</div><div>in shop.html at the end of every product we check<br>if<br></div><div>the user is logged in and if the user is a admin, if</div><div>both<br>are true we display a edit button which redirect to item page</div><div>with the<br>product details.</div><div>Same for item details page, if the user is a</div><div>admin we display<br>the edit button.</div><div>The admin items page has edit button default</div><div>as the page is<br>only accessed by admin.</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vd345-prod.herokuapp.com/">https://is601-vd345-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233866502-ab6c5a4c-b8c9-4c93-a89a-66743ff5b2f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>view of shop page, clicking on name of the product it takes you<br>to the product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233866525-f0fbc76c-939e-4abe-b6e4-e0c238651702.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>product details page of 2nd item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>Created itemdetails.html &amp;&nbsp; itemdetails function for this.</div><div>Made the product name clickable, when clicked</div><div>will<br>pass the product id to itemdetails function and get all details from</div><div>Products table<br>passing the id and render them in the itemdetails page.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vd345-prod.herokuapp.com/">https://is601-vd345-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233866651-246cec5b-e19f-4338-8c0e-3a3251c26bd5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message upon adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233866728-683d6f98-ce43-40bb-ab71-3dd07531f73a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message when a user is trying to add to cart without logging<br>in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233866836-93dd0442-eb8b-4d1c-b519-7c9c301c6e32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart table from Database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>1 cart per user, having product_id &amp; user_id as composite unique key<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <div>Clicking the ADD button, the product id as hidden field, quantity field gets</div><div>submitted<br>to cart function in shop.py,&nbsp;</div><div><br></div><div>and as the product id is passed and</div><div>quantity is<br>greater than 0, we insert the product id, user id, desired</div><div>quantity, and unit_price(fetching<br>it from products table)</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867272-99c75c57-f79c-4df7-a5a4-feaf06f7cc46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the cart with products.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div>When we click the cart, the cart function checking there is no product</div><div>id<br>being passed knows that this is not a add or update function</div><div>and goes<br>to SELECT block getting, id, product id, name, desired quantity and</div><div>calculates the subtotal<br>multiplying the desired quantity and unit_price in select statement only,</div><div>passing user id. and<br>passes these values to cart.html.</div><div><br></div><div>For the total calculation,&nbsp;</div><div>we render</div><div>each item as a row<br>in table in the HTML output and and</div><div>for every row we add the<br>subtotal value to the a variable ns.total</div><div>and later display it as Total in<br>the bottom.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vd345-prod.herokuapp.com/">https://is601-vd345-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867341-aa0033e8-1df6-490f-8098-3ec1cd3ed053.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before updating the quantity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867377-08d03258-094e-48bb-873b-ec326439a43d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after updating the quantity of Shirt for men  to 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867462-6338b20b-38e4-4548-a9dc-0920270ba16d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before updating the quantity to zero<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867531-34899c5f-6f0f-4fc3-961c-353f113d15f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after updating the quantity of electronics &amp; services to zero, so it<br>got deleted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867716-374860d6-561b-47a5-83a9-af5ee6995e78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>gave the HTML input quantity field a attribute min=&quot;0&quot;, so it does not<br>allow negative values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>In the cart,</div><div><br></div><div>Beside the quantity field &amp; update button a hidden product id</div><div>will<br>be passed to the cart function when we click the update button.</div><div>And in<br>the code if the quantity &gt; 0,&nbsp;</div><div>First we get the price</div><div>&amp; name from<br>products table, then we update the quantity &amp; price in</div><div>cart table passing product<br>id &amp; user id.</div><div>When we pass the 0 in</div><div>quantity field, as the quantity<br>is less than 0, the code goes to</div><div>DELETE block, we delete the product<br>from cart table passing product id &amp;</div><div>user id.</div><div><br></div><div>For the negative value handling in<br>quantity field, we set the min</div><div>value for the input field as 0 in<br>HTML.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867960-e93b8e63-6e0c-47ed-8d6a-1b37cca8b365.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before deleting a single item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233867933-2dd285ee-e3dc-4814-a1e5-2fbf2182213c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after deleting a item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233868061-4707ebf9-d538-4307-a39d-15615bcb460b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before clearing it<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123218376/233868072-cf257da8-9631-45f1-a3c8-b603a5a5bf74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after clearing all items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>When deleting a single item in cart,</div><div>Beside the delete button, a hidden field<br></div><div>quantity<br>of -1 will be submitted and in the cart function when the</div><div>quantity is<br>less than zero, it processes the Delete query passing product id.</div><div>When clearing the<br>total cart,we pass a variable delete_all equal to 1, and in<br></div><div>the cart function,<br>if the delete_all value is True we delete the records</div><div>in Cart table passing<br>user_id.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23">https://github.com/vijayasindhudandeboina/IS601-006SPRING/pull/23</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Stuck at clearing the cart for some time, but later got the idea</div><div>to<br>set a variable and passing it when clearing the cart, and checking</div><div>the value<br>in code to do the rest of the work.</div><div>And the other point stuck<br>at is displaying the shop public page when no user is<br></div><div>logged in, initially<br>did not write the if condition for authentication around edit</div><div>button and got an<br>error at that place as without the user logged</div><div>in the code is checking<br>for admin role in current user.</div><div>later added the is_authenticated condition around admin condition.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vd345-prod.herokuapp.com/">https://is601-vd345-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vd345" target="_blank">Grading</a></td></tr></table>
