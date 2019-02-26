namespace PostsRegisterer
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pbox_postImage = new System.Windows.Forms.PictureBox();
            this.btn_skip = new System.Windows.Forms.Button();
            this.btn_exclude = new System.Windows.Forms.Button();
            this.btn_confirm = new System.Windows.Forms.Button();
            this.tb_phone = new System.Windows.Forms.TextBox();
            this.tb_price = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.btn_updateComments = new System.Windows.Forms.Button();
            this.tb_message = new System.Windows.Forms.RichTextBox();
            this.btn_updateDb = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pbox_postImage)).BeginInit();
            this.SuspendLayout();
            // 
            // pbox_postImage
            // 
            this.pbox_postImage.Location = new System.Drawing.Point(-1, 12);
            this.pbox_postImage.Name = "pbox_postImage";
            this.pbox_postImage.Size = new System.Drawing.Size(1088, 343);
            this.pbox_postImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pbox_postImage.TabIndex = 0;
            this.pbox_postImage.TabStop = false;
            // 
            // btn_skip
            // 
            this.btn_skip.Location = new System.Drawing.Point(901, 359);
            this.btn_skip.Name = "btn_skip";
            this.btn_skip.Size = new System.Drawing.Size(75, 32);
            this.btn_skip.TabIndex = 1;
            this.btn_skip.Text = "تخطي الان";
            this.btn_skip.UseVisualStyleBackColor = true;
            this.btn_skip.Click += new System.EventHandler(this.btn_skip_Click);
            // 
            // btn_exclude
            // 
            this.btn_exclude.Location = new System.Drawing.Point(994, 361);
            this.btn_exclude.Name = "btn_exclude";
            this.btn_exclude.Size = new System.Drawing.Size(83, 29);
            this.btn_exclude.TabIndex = 2;
            this.btn_exclude.Text = "ليس به رقم للبيع";
            this.btn_exclude.UseVisualStyleBackColor = true;
            this.btn_exclude.Click += new System.EventHandler(this.btn_exclude_Click);
            // 
            // btn_confirm
            // 
            this.btn_confirm.Location = new System.Drawing.Point(43, 392);
            this.btn_confirm.Name = "btn_confirm";
            this.btn_confirm.Size = new System.Drawing.Size(105, 66);
            this.btn_confirm.TabIndex = 3;
            this.btn_confirm.Text = "تأكيد الرقم والسعر";
            this.btn_confirm.UseVisualStyleBackColor = true;
            this.btn_confirm.Click += new System.EventHandler(this.btn_confirm_Click);
            // 
            // tb_phone
            // 
            this.tb_phone.Location = new System.Drawing.Point(164, 392);
            this.tb_phone.Name = "tb_phone";
            this.tb_phone.Size = new System.Drawing.Size(114, 22);
            this.tb_phone.TabIndex = 4;
            // 
            // tb_price
            // 
            this.tb_price.Location = new System.Drawing.Point(164, 436);
            this.tb_price.Name = "tb_price";
            this.tb_price.Size = new System.Drawing.Size(114, 22);
            this.tb_price.TabIndex = 5;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(297, 392);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 17);
            this.label1.TabIndex = 6;
            this.label1.Text = "رقم المحمول";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(297, 436);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(34, 17);
            this.label2.TabIndex = 7;
            this.label2.Text = "السعر";
            // 
            // btn_updateComments
            // 
            this.btn_updateComments.Enabled = false;
            this.btn_updateComments.Font = new System.Drawing.Font("Microsoft Sans Serif", 25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_updateComments.Location = new System.Drawing.Point(774, 63);
            this.btn_updateComments.Name = "btn_updateComments";
            this.btn_updateComments.Size = new System.Drawing.Size(271, 120);
            this.btn_updateComments.TabIndex = 8;
            this.btn_updateComments.Text = "تعديل وتعليق علي جميع الكومنتات";
            this.btn_updateComments.UseVisualStyleBackColor = true;
            this.btn_updateComments.Visible = false;
            this.btn_updateComments.Click += new System.EventHandler(this.btn_updateComments_Click);
            // 
            // tb_message
            // 
            this.tb_message.AcceptsTab = true;
            this.tb_message.Location = new System.Drawing.Point(402, 364);
            this.tb_message.Name = "tb_message";
            this.tb_message.Size = new System.Drawing.Size(308, 121);
            this.tb_message.TabIndex = 9;
            this.tb_message.Text = "";
            // 
            // btn_updateDb
            // 
            this.btn_updateDb.Enabled = false;
            this.btn_updateDb.Font = new System.Drawing.Font("Microsoft Sans Serif", 25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_updateDb.Location = new System.Drawing.Point(134, 63);
            this.btn_updateDb.Name = "btn_updateDb";
            this.btn_updateDb.Size = new System.Drawing.Size(271, 120);
            this.btn_updateDb.TabIndex = 11;
            this.btn_updateDb.Text = "اعاده رفع الردود التلقائية";
            this.btn_updateDb.UseVisualStyleBackColor = true;
            this.btn_updateDb.Visible = false;
            this.btn_updateDb.Click += new System.EventHandler(this.registerToFirebase);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1089, 518);
            this.Controls.Add(this.btn_updateDb);
            this.Controls.Add(this.tb_message);
            this.Controls.Add(this.btn_updateComments);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tb_price);
            this.Controls.Add(this.tb_phone);
            this.Controls.Add(this.btn_confirm);
            this.Controls.Add(this.btn_exclude);
            this.Controls.Add(this.btn_skip);
            this.Controls.Add(this.pbox_postImage);
            this.Name = "Form1";
            this.Text = "Form1";
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pbox_postImage)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pbox_postImage;
        private System.Windows.Forms.Button btn_skip;
        private System.Windows.Forms.Button btn_exclude;
        private System.Windows.Forms.Button btn_confirm;
        private System.Windows.Forms.TextBox tb_phone;
        private System.Windows.Forms.TextBox tb_price;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btn_updateComments;
        private System.Windows.Forms.RichTextBox tb_message;
        private System.Windows.Forms.Button btn_updateDb;
    }
}

