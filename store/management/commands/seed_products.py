from django.core.management.base import BaseCommand
from store.models import Product, Category


class Command(BaseCommand):
    help = "Seed products into the database"

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()

        men = Category.objects.get(name="Men")

        products = [

            {
                "category": men,
                "name": "Classic Cotton T-Shirt",
                "price": 799,
                "description": "Made from 100% premium cotton, this t-shirt offers superior comfort, breathability, and durability. Its regular fit and soft fabric make it an ideal choice for everyday wear, casual outings, and all-day comfort.",
                "image": "products/men/tshirt1.jpg",
            },

            {
                "category": men,
                "name": "Slim Fit Jeans",
                "price": 1499,
                "description": "Crafted from high-quality stretch denim, these slim-fit jeans provide a stylish appearance with exceptional comfort. Perfect for casual outings, office wear, and weekend adventures.",
                "image": "products/men/jeans1.jpg",
            },

            {
                "category": men,
                "name": "Formal White Shirt",
                "price": 1299,
                "description": "Designed with premium breathable fabric, this formal shirt delivers a crisp and elegant look. Ideal for business meetings, office wear, interviews, and special occasions.",
                "image": "products/men/shirt1.jpg",
            },

            {
                "category": men,
                "name": "Casual Checked Shirt",
                "price": 1399,
                "description": "A fashionable checked shirt made from soft cotton fabric that provides lasting comfort throughout the day. Perfect for casual gatherings, travel, and everyday styling.",
                "image": "products/men/shirt2.jpg",
            },

            {
                "category": men,
                "name": "Polo T-Shirt",
                "price": 999,
                "description": "This premium polo t-shirt features a classic collar and breathable fabric for a sophisticated yet casual appearance. Suitable for office casuals, outings, and everyday fashion.",
                "image": "products/men/polo1.jpg",
            },

            {
                "category": men,
                "name": "Leather Jacket",
                "price": 3499,
                "description": "Crafted from premium-quality leather with a modern slim-fit design, this jacket offers warmth, durability, and timeless style. Perfect for winter seasons, bike rides, and evening outings.",
                "image": "products/men/jacket1.jpg",
            },

            {
                "category": men,
                "name": "Cargo Pants",
                "price": 1599,
                "description": "Designed with multiple utility pockets and durable fabric, these cargo pants combine comfort with functionality. Ideal for travel, outdoor activities, and everyday casual wear.",
                "image": "products/men/cargo1.jpg",
            },

            {
                "category": men,
                "name": "Chino Pants",
                "price": 1699,
                "description": "Premium slim-fit chino pants made from soft and stretchable fabric for maximum comfort. A perfect choice for office wear, casual meetings, and weekend outings.",
                "image": "products/men/chino1.jpg",
            },

            {
                "category": men,
                "name": "Winter Hoodie",
                "price": 1899,
                "description": "Stay warm during cold weather with this fleece-lined hoodie featuring a comfortable fit and premium fabric. Suitable for travel, workouts, and daily winter wear.",
                "image": "products/men/hoodie1.jpg",
            },

            {
                "category": men,
                "name": "Premium Blazer",
                "price": 3999,
                "description": "An elegant tailored blazer crafted with premium fabric for a polished appearance. Perfect for business meetings, weddings, formal occasions, and professional events.",
                "image": "products/men/blazer1.jpg",
            },

        ]

        women = Category.objects.get(name="Women")

        products.extend([

            {
                "category": women,
                "name": "Floral Maxi Dress",
                "price": 1899,
                "description": "Elegant floral maxi dress made from soft and breathable fabric for all-day comfort. Its stylish design makes it perfect for parties, vacations, casual outings, and family gatherings. Pair it with heels or flats to create a graceful and fashionable look.",
                "image": "products/women/dress1.jpg",
            },

            {
                "category": women,
                "name": "Party Wear Dress",
                "price": 3499,
                "description": "Beautiful party wear dress designed with premium-quality fabric and a modern fit. Ideal for weddings, evening parties, birthdays, and festive celebrations. The elegant design adds confidence and charm to your overall appearance.",
                "image": "products/women/dress2.jpg",
            },

            {
                "category": women,
                "name": "Cotton Kurti",
                "price": 999,
                "description": "Comfortable cotton kurti crafted with breathable fabric for everyday elegance and comfort. Perfect for office wear, college, casual outings, and daily use. The lightweight material ensures freshness throughout the day.",
                "image": "products/women/kurti1.jpg",
            },

            {
                "category": women,
                "name": "Casual Top",
                "price": 799,
                "description": "Stylish casual top designed with soft fabric and a comfortable fit for everyday fashion. Perfect for shopping, travel, college, and casual outings. Easily pairs with jeans, skirts, or trousers for a trendy look.",
                "image": "products/women/top1.jpg",
            },

            {
                "category": women,
                "name": "Designer Top",
                "price": 999,
                "description": "Premium designer top featuring a modern style and elegant finish for a fashionable appearance. Suitable for parties, casual events, and weekend outings. Designed to provide both comfort and confidence wherever you go.",
                "image": "products/women/top2.jpg",
            },

            {
                "category": women,
                "name": "Denim Jacket",
                "price": 2299,
                "description": "Classic denim jacket made with durable premium fabric for a timeless fashion statement. Perfect for every season and easy to pair with dresses, jeans, or tops. Offers both comfort and effortless style for everyday wear.",
                "image": "products/women/jacket2.jpg",
            },

            {
                "category": women,
                "name": "Women's Jeans",
                "price": 1499,
                "description": "Slim-fit stretchable jeans designed to provide maximum comfort and flexibility throughout the day. Suitable for casual outings, travel, shopping, and everyday wear. The premium denim fabric ensures durability and a stylish appearance.",
                "image": "products/women/jeans2.jpg",
            },

            {
                "category": women,
                "name": "Printed Skirt",
                "price": 1199,
                "description": "Fashionable printed skirt made from lightweight and comfortable fabric for effortless everyday style. Perfect for vacations, casual outings, and summer wear. Its elegant design adds a fresh and trendy touch to your wardrobe.",
                "image": "products/women/skirt1.jpg",
            },

            {
                "category": women,
                "name": "Winter Hoodie",
                "price": 1699,
                "description": "Warm fleece hoodie designed to keep you comfortable during cold weather without compromising style. Ideal for travel, workouts, outdoor activities, and daily winter wear. The soft fabric provides lasting warmth and comfort.",
                "image": "products/women/hoodie2.jpg",
            },

            {
                "category": women,
                "name": "Women's Blazer",
                "price": 2899,
                "description": "Elegant women's blazer tailored with premium fabric for a polished and sophisticated look. Perfect for office meetings, business events, interviews, and formal occasions. Its modern fit enhances confidence while ensuring all-day comfort.",
                "image": "products/women/blazer2.jpg",
            },

        ])

        footwear = Category.objects.get(name="Footwear")

        products.extend([

            {
                "category": footwear,
                "name": "Running Shoes",
                "price": 2499,
                "description": "Experience superior comfort with these lightweight running shoes designed for daily workouts and jogging. The breathable mesh upper and cushioned sole provide excellent support and flexibility. Perfect for running, gym sessions, walking, and everyday activities.",
                "image": "products/footwear/shoe1.jpg",
            },

            {
                "category": footwear,
                "name": "White Sneakers",
                "price": 1999,
                "description": "Upgrade your casual style with these premium white sneakers featuring a modern and trendy design. Built with soft cushioning and durable materials for all-day comfort. Ideal for college, travel, shopping, and everyday fashion.",
                "image": "products/footwear/shoe2.jpg",
            },

            {
                "category": footwear,
                "name": "Sports Shoes",
                "price": 2799,
                "description": "High-performance sports shoes designed to deliver comfort, stability, and excellent grip on every step. The breathable construction keeps your feet fresh during long hours of activity. Perfect for sports, fitness training, and outdoor adventures.",
                "image": "products/footwear/shoe3.jpg",
            },

            {
                "category": footwear,
                "name": "Formal Leather Shoes",
                "price": 3299,
                "description": "Premium leather formal shoes crafted with an elegant finish for a sophisticated look. Designed to provide maximum comfort throughout office hours and formal events. A perfect choice for business meetings, interviews, and special occasions.",
                "image": "products/footwear/shoe4.jpg",
            },

            {
                "category": footwear,
                "name": "Casual Loafers",
                "price": 1899,
                "description": "Stylish slip-on loafers made from premium-quality materials for everyday comfort and convenience. Their lightweight design makes them ideal for long hours of wear without discomfort. Suitable for office, travel, and casual outings.",
                "image": "products/footwear/shoe5.jpg",
            },

            {
                "category": footwear,
                "name": "Leather Boots",
                "price": 4299,
                "description": "Premium leather boots built with durable materials to provide long-lasting performance and comfort. The rugged design offers excellent grip and protection in all weather conditions. Perfect for winter wear, trekking, and outdoor adventures.",
                "image": "products/footwear/shoe6.jpg",
            },

            {
                "category": footwear,
                "name": "Comfort Sandals",
                "price": 999,
                "description": "Soft cushioned sandals designed to provide superior comfort during everyday use. Adjustable straps ensure a secure fit while the lightweight sole reduces foot fatigue. Ideal for home, travel, and casual outdoor activities.",
                "image": "products/footwear/shoe7.jpg",
            },

            {
                "category": footwear,
                "name": "Flip Flops",
                "price": 599,
                "description": "Comfortable flip flops featuring lightweight construction and anti-slip soles for better stability. Designed for relaxed daily wear, beach trips, and indoor use. Easy to clean and perfect for all-day comfort.",
                "image": "products/footwear/shoe8.jpg",
            },


        ])
        watches = Category.objects.get(name="Watches")

        products.extend([

            {
                "category": watches,
                "name": "Classic Analog Watch",
                "price": 2499,
                "description": "Experience timeless elegance with this classic analog watch, crafted with a premium finish and a durable stainless-steel case. Its comfortable strap and stylish dial make it perfect for office wear, business meetings, and everyday use.",
                "image": "products/watches/watch.jpg",
            },

            {
                "category": watches,
                "name": "Smart Watch",
                "price": 4999,
                "description": "Stay connected and monitor your health with this advanced smartwatch featuring fitness tracking, heart-rate monitoring, and smart notifications. Its modern design and long-lasting battery make it ideal for daily use and workouts.",
                "image": "products/watches/watch1.jpg",
            },

            {
                "category": watches,
                "name": "Luxury Gold Watch",
                "price": 6999,
                "description": "Designed with a luxurious gold finish and premium craftsmanship, this elegant wristwatch adds sophistication to every outfit. Perfect for weddings, parties, business events, and other special occasions.",
                "image": "products/watches/watch2.jpg",
            },

            {
                "category": watches,
                "name": "Sports Digital Watch",
                "price": 1999,
                "description": "Built for active lifestyles, this digital sports watch features a durable design with water resistance, stopwatch, and alarm functions. Ideal for running, gym workouts, outdoor adventures, and everyday sports activities.",
                "image": "products/watches/watch3.jpg",
            },

            {
                "category": watches,
                "name": "Leather Strap Watch",
                "price": 2999,
                "description": "Crafted with a genuine leather strap and a stylish dial, this watch delivers both comfort and elegance. Its premium design makes it suitable for office wear, formal occasions, and everyday fashion.",
                "image": "products/watches/watch4.jpg",
            },

            {
                "category": watches,
                "name": "Luxury Silver Watch",
                "price": 4599,
                "description": "This premium silver wristwatch combines modern style with exceptional craftsmanship for a sophisticated appearance. Its polished finish and elegant dial make it a perfect accessory for both formal and casual wear.",
                "image": "products/watches/watch5.jpg",
            },

            {
                "category": watches,
                "name": "Minimal Black Watch",
                "price": 2799,
                "description": "Featuring a sleek black dial and minimalist design, this watch offers a modern and versatile look for any occasion. Lightweight, comfortable, and stylish, it complements both casual and professional outfits.",
                "image": "products/watches/watch6.jpg",
            },

            {
                "category": watches,
                "name": "Premium Chronograph Watch",
                "price": 5999,
                "description": "Designed with precision chronograph functionality and a premium stainless-steel finish, this watch offers both performance and luxury. A perfect choice for professionals, watch enthusiasts, and those who appreciate timeless craftsmanship.",
                "image": "products/watches/watch7.jpg",
            },

        ])

        electronics = Category.objects.get(name="Electronics")

        products.extend([

            {
                "category": electronics,
                "name": "Gaming Laptop",
                "price": 69999,
                "description": "Experience powerful performance with this high-speed gaming laptop featuring a fast processor, dedicated graphics, and a Full HD display. Perfect for gaming, programming, video editing, and professional work with smooth multitasking capabilities.",
                "image": "products/electronics/laptop1.jpg",
            },

            {
                "category": electronics,
                "name": "Android Smartphone",
                "price": 24999,
                "description": "Stay connected with this feature-packed Android smartphone offering a vibrant display, powerful processor, and long-lasting battery life. Capture stunning photos, enjoy smooth performance, and experience seamless multitasking every day.",
                "image": "products/electronics/phone1.jpg",
            },

            {
                "category": electronics,
                "name": "Wireless Headphones",
                "price": 3999,
                "description": "Enjoy crystal-clear audio with these premium wireless headphones featuring deep bass, noise isolation, and long battery life. Designed for music lovers, gaming, online meetings, and everyday entertainment with maximum comfort.",
                "image": "products/electronics/headphones.jpg",
            },

            {
                "category": electronics,
                "name": "Gaming Headset",
                "price": 2999,
                "description": "Experience immersive surround sound with this gaming headset featuring a noise-cancelling microphone and soft ear cushions. Perfect for gaming, streaming, online classes, and professional communication without distractions.",
                "image": "products/electronics/headphone1.jpg",
            },

            {
                "category": electronics,
                "name": "Bluetooth Speaker",
                "price": 2999,
                "description": "Bring your music to life with this portable Bluetooth speaker delivering powerful sound, deep bass, and long-lasting battery backup. Ideal for home entertainment, travel, outdoor adventures, and parties.",
                "image": "products/electronics/speaker1.jpg",
            },

            {
                "category": electronics,
                "name": "DSLR Camera",
                "price": 54999,
                "description": "Capture professional-quality photos and videos with this advanced DSLR camera featuring high-resolution imaging and powerful autofocus. Perfect for photography enthusiasts, content creators, travel, and special occasions.",
                "image": "products/electronics/camera1.jpg",
            },

            {
                "category": electronics,
                "name": "Android Tablet",
                "price": 18999,
                "description": "Enjoy a large HD display and smooth performance with this lightweight Android tablet designed for learning, entertainment, reading, and office work. Its long-lasting battery makes it an excellent companion for daily use.",
                "image": "products/electronics/tablet1.jpg",
            },

            {
                "category": electronics,
                "name": "Wireless Earbuds",
                "price": 2499,
                "description": "Listen to your favorite music with these compact wireless earbuds featuring crystal-clear sound, touch controls, and fast charging support. Designed for workouts, travel, office use, and uninterrupted entertainment.",
                "image": "products/electronics/earbuds1.jpg",
            },

            {
                "category": electronics,
                "name": "Smart Fitness Watch",
                "price": 3499,
                "description": "Track your daily fitness goals with this smart fitness watch featuring heart-rate monitoring, step counting, sleep tracking, and smart notifications. Its stylish design and long battery life make it perfect for everyday use.",
                "image": "products/electronics/watch8.jpg",
            },

        ])

        bags = Category.objects.get(name="Bags")

        products.extend([

            {
                "category": bags,
                "name": "Leather Office Bag",
                "price": 2499,
                "description": "Carry your essentials in style with this premium leather office bag, designed for professionals who value elegance and functionality. It features spacious compartments for laptops, documents, and accessories, making it perfect for office, business meetings, and daily use.",
                "image": "products/bags/bag.jpg",
            },

            {
                "category": bags,
                "name": "Travel Backpack",
                "price": 1999,
                "description": "Designed for comfort and convenience, this spacious travel backpack offers multiple storage compartments and adjustable padded shoulder straps. Perfect for travel, office, college, and everyday adventures with excellent durability.",
                "image": "products/bags/bag1.jpg",
            },

            {
                "category": bags,
                "name": "Laptop Backpack",
                "price": 2299,
                "description": "Protect your laptop with this stylish backpack featuring a padded laptop compartment and multiple organizer pockets. Its lightweight design and comfortable straps make it ideal for work, college, travel, and daily commuting.",
                "image": "products/bags/bag2.jpg",
            },

            {
                "category": bags,
                "name": "Crossbody Sling Bag",
                "price": 1499,
                "description": "This compact crossbody sling bag combines modern style with everyday practicality, offering enough space for your phone, wallet, keys, and essentials. Perfect for shopping, travel, casual outings, and daily use.",
                "image": "products/bags/bag3.jpg",
            },

            {
                "category": bags,
                "name": "Women's Handbag",
                "price": 2799,
                "description": "Enhance your style with this elegant women's handbag crafted from premium-quality materials and a sophisticated design. Spacious enough for your daily essentials, it's perfect for office, shopping, parties, and special occasions.",
                "image": "products/bags/bag4.jpg",
            },

            {
                "category": bags,
                "name": "Duffel Gym Bag",
                "price": 1799,
                "description": "Stay organized with this spacious duffel gym bag featuring multiple compartments for clothes, shoes, water bottles, and workout accessories. Built with durable fabric, it's ideal for gym sessions, sports, and short trips.",
                "image": "products/bags/bag5.jpg",
            },

            {
                "category": bags,
                "name": "School Backpack",
                "price": 1599,
                "description": "Designed for students and professionals, this comfortable backpack offers multiple compartments for books, laptops, stationery, and daily essentials. Its durable construction and ergonomic design ensure long-lasting comfort and reliability.",
                "image": "products/bags/bag6.jpg",
            },

        ])


        for item in products:
            Product.objects.create(**item)

        self.stdout.write(
            self.style.SUCCESS("products added successfully!")
        )