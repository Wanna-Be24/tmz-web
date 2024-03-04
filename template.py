def generate_grid_container(celebrity_name, face_image, central_image, be_real_items, be_like_items, date):
    template = f"""
    <div class="grid-container">
        <div class="card-header1">
            <img class="celebrity-photo" src="{face_image}" alt="{celebrity_name}">
            <div class="celebrity-info">
                <div class="celebrity-name">{celebrity_name}</div>
                <div class="date">{date}</div>
            </div>
        </div>
        <div class="left-column column">
            <div class="item title">Be Real:</div>
    """

    for item in be_real_items:
        template += f"""
            <div class="item text"><b>{item['name']}</b> - {item['description']}<br><b>${item['price']} <img src="./cart.svg" style="width: 20px; padding-bottom: 5px;"></b></div>
            <div class="item flexible"><img class="img-aspect-auto" src="{item['image']}" loading="lazy" alt=""></div>
        """

    template += """
        </div>
        <div class="column">
            <div class="center"><img width="342" height="512" class="img-aspect-auto" src="{central_image}" loading="lazy" alt="{celebrity_name}"></div>
        </div>
        <div class="right-column column">
            <div class="item title">Be Like:</div>
    """

    for item in be_like_items:
        template += f"""
            <div class="item text"><b>{item['name']}</b> - {item['description']}<br><b>${item['price']} <img src="./cart.svg" style="width: 20px; padding-bottom: 5px;"></b></div>
            <div class="item flexible"><img class="img-aspect-auto" src="{item['image']}" loading="lazy" alt=""></div>
        """

    template += """
        </div>
    </div>
    """

    return template

# Example usage
celebrity_name = "Taylor Swift"
face_image = "./taylor-swift/face.png"
central_image = "./taylor-swift/taylor-swift.png"
be_real_items = [
    {"name": "Bag Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_real/bag-removebg-preview.png"},
    {"name": "Suit Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_real/suit-removebg-preview.png"},
    {"name": "Dress Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_real/dress-removebg-preview.png"},

    # {"name": "Pants Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_real/pants-removebg-preview.png"},
    {"name": "Shoes Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_real/shoes.png"}

]
be_like_items = [
    {"name": "Bag Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_like/bag-removebg-preview.png"},
    {"name": "Suit Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_like/suit-removebg-preview.png"},
    {"name": "Dress Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_like/dress-removebg-preview.png"},

    # {"name": "Pants Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_like/pants-removebg-preview.png"},
    {"name": "Shoes Brand", "description": "Description", "price": "Price", "image": "./taylor-swift/be_like/shoes-removebg-preview.png"}
]
date = "March 4, 2024"

html_template = generate_grid_container(celebrity_name, face_image, central_image, be_real_items, be_like_items, date)
print(html_template)
