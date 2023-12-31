PGDMP  $                
    {            Sweets    14.5    16.1 !    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16405    Sweets    DATABASE     |   CREATE DATABASE "Sweets" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "Sweets";
                postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            �           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    4            �            1259    16444    Suger    TABLE     �   CREATE TABLE public."Suger" (
    id integer NOT NULL,
    name character varying,
    description character varying,
    category_id integer,
    img character varying
);
    DROP TABLE public."Suger";
       public         heap    postgres    false    4            �            1259    16443    Suger_id_seq    SEQUENCE     �   CREATE SEQUENCE public."Suger_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public."Suger_id_seq";
       public          postgres    false    4    214            �           0    0    Suger_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public."Suger_id_seq" OWNED BY public."Suger".id;
          public          postgres    false    213            �            1259    16407    category    TABLE     Z   CREATE TABLE public.category (
    id integer NOT NULL,
    category character varying
);
    DROP TABLE public.category;
       public         heap    postgres    false    4            �            1259    16406    category_id_seq    SEQUENCE     �   CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.category_id_seq;
       public          postgres    false    210    4            �           0    0    category_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;
          public          postgres    false    209            �            1259    16433    response    TABLE     Y   CREATE TABLE public.response (
    id integer NOT NULL,
    comment character varying
);
    DROP TABLE public.response;
       public         heap    postgres    false    4            �            1259    16432    response_id_seq    SEQUENCE     �   CREATE SEQUENCE public.response_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.response_id_seq;
       public          postgres    false    212    4            �           0    0    response_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.response_id_seq OWNED BY public.response.id;
          public          postgres    false    211                       2604    16447    Suger id    DEFAULT     h   ALTER TABLE ONLY public."Suger" ALTER COLUMN id SET DEFAULT nextval('public."Suger_id_seq"'::regclass);
 9   ALTER TABLE public."Suger" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213    214                       2604    16410    category id    DEFAULT     j   ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);
 :   ALTER TABLE public.category ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    210    210                       2604    16436    response id    DEFAULT     j   ALTER TABLE ONLY public.response ALTER COLUMN id SET DEFAULT nextval('public.response_id_seq'::regclass);
 :   ALTER TABLE public.response ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    211    212    212            �          0    16444    Suger 
   TABLE DATA           J   COPY public."Suger" (id, name, description, category_id, img) FROM stdin;
    public          postgres    false    214   �        �          0    16407    category 
   TABLE DATA           0   COPY public.category (id, category) FROM stdin;
    public          postgres    false    210   �#       �          0    16433    response 
   TABLE DATA           /   COPY public.response (id, comment) FROM stdin;
    public          postgres    false    212   Z$       �           0    0    Suger_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."Suger_id_seq"', 5, true);
          public          postgres    false    213            �           0    0    category_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.category_id_seq', 7, true);
          public          postgres    false    209            �           0    0    response_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.response_id_seq', 2, true);
          public          postgres    false    211                       2606    16451    Suger Suger_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public."Suger"
    ADD CONSTRAINT "Suger_pkey" PRIMARY KEY (id);
 >   ALTER TABLE ONLY public."Suger" DROP CONSTRAINT "Suger_pkey";
       public            postgres    false    214                       2606    16414    category category_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.category DROP CONSTRAINT category_pkey;
       public            postgres    false    210                       2606    16440    response response_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.response
    ADD CONSTRAINT response_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.response DROP CONSTRAINT response_pkey;
       public            postgres    false    212                       1259    16457    ix_Suger_id    INDEX     ?   CREATE INDEX "ix_Suger_id" ON public."Suger" USING btree (id);
 !   DROP INDEX public."ix_Suger_id";
       public            postgres    false    214                       1259    16415    ix_category_category    INDEX     M   CREATE INDEX ix_category_category ON public.category USING btree (category);
 (   DROP INDEX public.ix_category_category;
       public            postgres    false    210                       1259    16416    ix_category_id    INDEX     A   CREATE INDEX ix_category_id ON public.category USING btree (id);
 "   DROP INDEX public.ix_category_id;
       public            postgres    false    210                       1259    16441    ix_response_comment    INDEX     K   CREATE INDEX ix_response_comment ON public.response USING btree (comment);
 '   DROP INDEX public.ix_response_comment;
       public            postgres    false    212                       1259    16442    ix_response_id    INDEX     A   CREATE INDEX ix_response_id ON public.response USING btree (id);
 "   DROP INDEX public.ix_response_id;
       public            postgres    false    212                       2606    16452    Suger Suger_category_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Suger"
    ADD CONSTRAINT "Suger_category_id_fkey" FOREIGN KEY (category_id) REFERENCES public.category(id);
 J   ALTER TABLE ONLY public."Suger" DROP CONSTRAINT "Suger_category_id_fkey";
       public          postgres    false    214    3089    210            �   �  x�}T�n�@];_����g\�)rb�1Imˏ"�JS*�ZQ��BHH,CU�n���p�G�k7E�%�̹��q'�B�iCK<���kZ�h��*h]]P��ZT�����՜Q�q]٬����6�R4e�e�3U�L����^u�\��i�z�Gi����u!uU�M�'M���ۦ��E��X��p쇓@�"G�'сEY$z��"�o��S&'�:�%�U�:nӦ�A�hE�B�q̔!e�%@[�|P]����ײ'w���ܪn���p�eӸ���)�V�j�)�G"�C��A�FO�lG�t�oJ�[�@<�����I����Y w2v31�'���Q�a(�	�o�d��T��6Nh{�^GݩN�/���z�g38�U��m:�x�vj��^,
����]pu�����a���\Ӆ&UͰ4��4K�5i�7=��CMw^�f��T�#|cg�Q�D!�[g�9�|�po/��4ϱ�n�emx0�N��NC�Dq`Ҙ���$��@jR�=u�&Y��y䏂D�{`��,�ޣ�-_�o̃~����x4��oԏ��z��x��]g@���������!�s��W�9�EP#��nqОog3�MG��Jh�%��{�|0�3x~�n���M��bg=Xw�+��	+�C7s����a"c�t��`Y�����I�05�}[��e��=9�#�v�;�<�>p<���"#۴1"�c[j:t�~_ӥl=�Z���g�      �   n   x�%�A
�@�3�	h�|&�	x� x�@ /X�%�Ƽ��G͵��;�Dk�l��,������j��H,r���Qcw-��Wk>n�f���@����>�f"�?\O��)�G"      �      x�3���2�,**����� I2     